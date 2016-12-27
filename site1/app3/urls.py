from django.conf.urls import url, include
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from . import models
from . import views

urlpatterns = [
    url(r'^$', ListView.as_view(model=models.Author),name='list'),
    # url(r'^/(?P<pk>\d+)$', DetailView.as_view(model=models.Author),name='detail'),
    url(r'^create/$', views.AuthorCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)$', views.AuthorUpdateView.as_view(),name='update'),


]
