from django.conf.urls import url, include
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from . import models
from . import views

urlpatterns = [
    url(r'^manage_books/$', views.manage_books,name='manage_books'),
    url(r'^manage_books/(?P<id_author>\d+)$', views.manage_books, name='manage_books_id_author'),
    url(r'^list$', ListView.as_view(model=models.Author),name='list'),
    # regular formsets
]
