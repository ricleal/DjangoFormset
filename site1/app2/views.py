from django.shortcuts import render, redirect, reverse
from .models import Author, Book
from .forms import AuthorForm, BookForm

from django.forms.models import inlineformset_factory

def manage_books(request, id_author=None):

    if id_author is None:
        # New
        author = Author()
        BookInlineFormSet = inlineformset_factory(Author, Book, form=BookForm, extra=3, can_delete=False)
    else:
        # Edit
        author = Author.objects.get(pk=id_author)
        BookInlineFormSet = inlineformset_factory(Author, Book, form=BookForm, extra=1, can_delete=True)


    if request.method == "POST":
        post_copy = request.POST.copy()
        if 'add_form' in request.POST:
            post_copy['nested-TOTAL_FORMS'] = int(post_copy['nested-TOTAL_FORMS'])+ 1

        form = AuthorForm(post_copy, request.FILES, instance=author, prefix="main")
        formset = BookInlineFormSet(post_copy, request.FILES, instance=author, prefix="nested")

        if 'add_form' not in request.POST and form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect(reverse('app2:list'))
    else:
        form = AuthorForm(instance=author, prefix="main")
        formset = BookInlineFormSet(instance=author, prefix="nested")

    return render(request, "app2/book_form.html", {"form":form, "formset": formset})
