from .models import Author, Book

from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

class AuthorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('name'),
        )
        super(AuthorForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Author
        fields = '__all__'

class BookForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('title'),
        )
        super(BookForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Book
        fields = '__all__'
