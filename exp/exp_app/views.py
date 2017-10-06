from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
import requests


def lotteryPane(request):
    r = requests.get('http://models-api:8000/lotteries')
    response = JsonResponse(r.json(), safe=False)
    return response


def cardPane(request):
    r = requests.get('http://models-api:8000/cards')
    response = JsonResponse(r.json(), safe=False)
    return response


def lotteryDetail(request, pk):
    r = requests.get('http://models-api:8000/lottery/' + pk)
    response = JsonResponse(r.json(), safe=False)
    return response


def cardDetail(request, pk):
    r = requests.get('http://models-api:8000/card/' + pk)
    response = JsonResponse(r.json(), safe=False)
    return response
