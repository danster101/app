import json
import socket
import sys
import time

from elasticsearch import Elasticsearch
from kafka import KafkaConsumer
from kafka.common import NodeNotReadyError


def es_add(pk, new_listing, es_hook, es_index, refresh=False):
    # FIX: for now use 'title' as the id, but I think this should use the serializer's id instead so that
    # titles don't have to be unique. This would require the id data to be returned by the post request
    # in the exp layer after the new lottery has been assigned a unique id in the model layer
    es_hook.index(index=es_index, doc_type='listing', id=pk, body=new_listing)
    if refresh:
        es_hook.indices.refresh(index=es_index)


def load_fixtures(es_hook):
    with open('../data/db.json', 'r') as db:
        data = json.loads(db.read())
    for data_row in data:
        if data_row['model'] == 'models_app.lottery':
            es_add(data_row['pk'], data_row['fields'], es_hook, 'lottery_index')
        elif data_row['model'] == 'models_app.card':
            es_add(data_row['pk'], data_row['fields'], es_hook, 'card_index')
    es_hook.indices.refresh(index='*')


def listen(es_hook, kafka_hook):
    for message in kafka_hook:
        # add each new addition to ES
        new_listing = json.loads(message.value.decode('utf-8'))
        pk = new_listing.pop('id', new_listing['title'])

        # NOTE: there is probably a better way to differentiate between cards and lotteries...
        if 'start_time' in new_listing:
            new_listing['start_time'] = new_listing['start_time'].replace(' ', 'T', 1)
            new_listing['end_time'] = new_listing['end_time'].replace(' ', 'T', 1)
            print(new_listing)
            try:
                es_add(pk, new_listing, es_hook, 'lottery_index', refresh=True)
            except:
                print('Elastic Search could not add the following lottery:', new_listing)
        else:
            print(new_listing)
            try:
                es_add(pk, new_listing, es_hook, 'card_index', refresh=True)
            except:
                print('Elastic Search could not add the following card:', new_listing)


def try_connect():
    # use socket to attempt to connect to es
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((str(sys.argv[1]), 9200))
        if result == 0:
            break
        else:
            time.sleep(3)

    # we should be connected by now
    es = Elasticsearch(['es'])

    # clear indices, rebuild from scratch
    es.indices.delete(index='*')

    # using try/catch seems to work better for kafka, as it dies/restarts
    # which can trick the socket check into thinking it's on when
    # in reality it just turned back off
    while True:
        try:
            consumer = KafkaConsumer('new_listing', group_id='indexer', bootstrap_servers=['kafka:9092'])
            break
        except NodeNotReadyError:
            time.sleep(3)

    load_fixtures(es)
    listen(es, consumer)


try_connect()
