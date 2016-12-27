from django.shortcuts import render, redirect, reverse
from .models import Author, Book
from .forms import AuthorForm, BookForm, BookInlineFormSetCreate, BookInlineFormSetEdit
from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView

from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView
from extra_views.generic import GenericInlineFormSet

# See:
# https://django-extra-views.readthedocs.io/en/latest/index.html

class BookInlineFormSetCreate(InlineFormSet):
    model = Book
    form_class = BookForm
    fields = '__all__'
    extra = 3
    can_delete=False

class BookInlineFormSetUpdate(InlineFormSet):
    model = Book
    form_class = BookForm
    fields = '__all__'
    extra = 1
    can_delete=True

# Create your views here.
class AuthorCreateView(CreateWithInlinesView):
    form_class = AuthorForm
    inlines = [BookInlineFormSetCreate]
    model = Author
    #inline_model = Book
    success_url = reverse_lazy('app3:list')

# Create your views here.
class AuthorUpdateView(UpdateWithInlinesView):
    form_class = AuthorForm
    inlines = [BookInlineFormSetUpdate]
    model = Author
    success_url = reverse_lazy('app3:list')
