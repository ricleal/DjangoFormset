from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect

import inspect

from . import models
from . import forms

# Create your views here.
class MusicianCreate(CreateView):
    model = models.Musician
    fields = ['first_name', 'last_name']

class FormsetMixin(object):
    object = None

    def get(self, request, *args, **kwargs):
        print(inspect.stack()[0].function)
        if 'pk' in kwargs:
            # For the UpdateView
            self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
        print(inspect.stack()[0].function)
        if 'pk' in kwargs:
            # For the UpdateView
            self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def get_formset_class(self):
        print(inspect.stack()[0].function)
        return self.formset_class

    def get_formset(self, formset_class):
        print(inspect.stack()[0].function)
        return formset_class(**self.get_formset_kwargs())

    def get_formset_kwargs(self):
        print(inspect.stack()[0].function)
        kwargs = {
            'instance': self.object
        }
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def form_valid(self, form, formset):
        print(inspect.stack()[0].function)
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return redirect(self.object.get_absolute_url())

    def form_invalid(self, form, formset):
        print(inspect.stack()[0].function)
        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class AlbumCreate(FormsetMixin,CreateView):
    template_name = 'app1/album_form.html'
    model = models.Musician
    form_class = forms.MusicianForm
    formset_class = forms.AlbumFormSetCreate

class AlbumEdit(FormsetMixin,UpdateView):
    template_name = 'app1/album_form.html'
    model = models.Musician
    form_class = forms.MusicianForm
    formset_class = forms.AlbumFormSetUpdate
