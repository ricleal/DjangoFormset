from django.forms import ModelForm
#from django.forms.models import modelformset_factory
from django.forms.models import inlineformset_factory
from app1.models import Musician, Album

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class MusicianForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MusicianForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.render_required_fields = True
        self.helper.render_hidden_fields = True
    class Meta:
        model = Musician
        fields = '__all__'

class AlbumForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.render_required_fields = True
        self.helper.render_hidden_fields = True
    class Meta:
        model = Album
        fields = '__all__'

AlbumFormSetCreate = inlineformset_factory(Musician, Album, form=AlbumForm, extra=3, can_delete=False)
AlbumFormSetUpdate = inlineformset_factory(Musician, Album, form=AlbumForm, extra=1, can_delete=True)
