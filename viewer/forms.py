from django.forms import ModelForm

from viewer.models import Genre


class GenreForm(ModelForm):
  class Meta:
    model = Genre
    fields = ['name']