from django.conf.urls import url, include
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from . import models
from . import views

urlpatterns = [
    url(r'^listmusician/$', ListView.as_view(model=models.Musician),name='listmusician'),
    url(r'^detailmusician/(?P<pk>\d+)/$', DetailView.as_view(model=models.Musician),name='detailmusician'),
    url(r'^createmusician/$', views.MusicianCreate.as_view()),

    url(r'^detailalbum/(?P<pk>\d+)/$', DetailView.as_view(model=models.Album),name='detailalbum'),
    # Formmsets with Class based views
    url(r'^createalbum/$', views.AlbumCreate.as_view()),
    url(r'^editalbum/(?P<pk>\d+)$', views.AlbumEdit.as_view()),
    # regular formsets

]
