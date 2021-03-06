from django.conf.urls import url

from . import views
from .auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lotteries/?$', views.lotteries, name='lotteries'),
    url(r'^lotteries/create/?$', views.lottery_create, name='lottery-create'),
    url(r'^lotteries/([0-9]+)/?$', views.lottery_detail, name='lottery-detail'),
    url(r'^cards/?$', views.cards, name='cards'),
    url(r'^cards/create/?$', views.card_create, name='card-create'),
    url(r'^cards/([0-9]+)/?$', views.card_detail, name='card-detail'),
    url(r'^search/?$', views.search, name='search'),

    url(r'^login/?$', auth_views.login, name='login'),
    url(r'^logout/?$', auth_views.logout, name='logout'),
    url(r'^register/?$', auth_views.register, name='register-user'),

    url(r'^.*$', views.bad_url, name='404'),
]
