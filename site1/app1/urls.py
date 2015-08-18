from django.conf.urls import patterns, url, include
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from . import models
from . import views

urlpatterns = [
    # url(r'^list/$', ListView.as_view(model=models.Musician),name='list'),
    # url(r'^detail/(?P<pk>\d+)/$', DetailView.as_view(model=models.Musician),name='detail'),
    # url(r'^create/$', views.MusicianCreate.as_view()),
]
