from django.conf.urls import patterns, url, include
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from . import models
from . import views

urlpatterns = [
    url(r'^listmusician/$', ListView.as_view(model=models.Musician),name='listmusician'),
    url(r'^detailmusician/(?P<pk>\d+)/$', DetailView.as_view(model=models.Musician),name='detailmusician'),
    url(r'^createmusician/$', views.MusicianCreate.as_view()),

    url(r'^createalbum/$', views.AlbumCreate.as_view()),
    url(r'^detailalbum/(?P<pk>\d+)/$', DetailView.as_view(model=models.Album),name='detailalbum'),
]
