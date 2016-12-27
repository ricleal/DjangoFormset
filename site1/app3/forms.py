from .models import Author, Book

from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML

class AuthorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.render_hidden_fields = True
    class Meta:
        model = Author
        fields = '__all__'

class BookForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.layout.append(HTML('<p>Some test html...</p>'))
        self.helper.render_hidden_fields = True

    class Meta:
        model = Book
        fields = '__all__'


# New
BookInlineFormSetCreate = inlineformset_factory(Author, Book, form=BookForm, extra=3, can_delete=False)
# Edit
BookInlineFormSetEdit = inlineformset_factory(Author, Book, form=BookForm, extra=1, can_delete=True)
