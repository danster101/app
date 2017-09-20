from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField()
    tokens = models.IntegerField()


class Lottery(models.Model):
    desc = models.CharField(max_length=200)
    users = models.ManyToManyField(User)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Bid(models.Model):
    lottery = models.ForeignKey(Lottery, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    value = models.IntegerField()


class Card(models.Model):
    lottery = models.ForeignKey(Lottery, models.SET_NULL)
    game = models.CharField(max_length=200)
    value = models.IntegerField(default=0)