from django.shortcuts import render, redirect, reverse
from .models import Author, Book
from .forms import AuthorForm, BookForm

from django.forms.models import inlineformset_factory

def manage_books(request, id_author=None):

    if id_author is None:
        author = Author()
        BookInlineFormSet = inlineformset_factory(Author, Book, form=BookForm, extra=2, can_delete=False)
    else:
        author = Author.objects.get(pk=id_author)
        BookInlineFormSet = inlineformset_factory(Author, Book, form=BookForm, extra=2, can_delete=True)


    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES, instance=author, prefix="main")
        formset = BookInlineFormSet(request.POST, request.FILES, instance=author, prefix="nested")

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect(reverse('app2:list'))
    else:
        form = AuthorForm(instance=author, prefix="main")
        formset = BookInlineFormSet(instance=author, prefix="nested")

    return render(request, "app2/book_form.html", {"form":form, "formset": formset})
