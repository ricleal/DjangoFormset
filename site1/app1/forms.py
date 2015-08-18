from django.forms import ModelForm
from django.forms.models import modelformset_factory
from app1.models import Musician, Album

class MusicianForm(ModelForm):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name']

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['artist', 'name', 'release_date', 'num_stars']

AlbumFormSet = inlineformset_factory(Sponsor, Album, form=AlbumForm, extra=2)
