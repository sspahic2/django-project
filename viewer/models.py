from django.db.models import Model, CharField


# Create your models here.

class Genre(Model):
  name = CharField(max_length=128)