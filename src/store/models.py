from django.db import models

# Create your models here.
ARTISTS = {
  'francis-cabrel': {'name': 'Francis Cabrel'},
  'lej': {'name': 'Elijay'},
  'rosana': {'name': 'Rosana'},
  'maria-dolores-pradera': {'name': 'María Dolores Pradera'},
}


ALBUMS = [
  {'name': 'Sarbacane', 'artists': [ARTISTS['francis-cabrel']]},
  {'name': 'La Dalle', 'artists': [ARTISTS['lej']]},
  {'name': 'Luna Nueva', 'artists': [ARTISTS['rosana'], ARTISTS['maria-dolores-pradera']]}
]

class Track(models.Model):
  """
  docstring
  """
  name          = models.CharField(max_length = 80)
  description   = models.TextField(blank=True)
  length        = models.CharField(max_length=10)
  artist        = models.CharField(max_length=50)
  contributed   = []
  state         = models.IntegerField()


class Artist(models.Model):
  """
  DEFINES AN ARTIST
  """
  name      = models.CharField(max_length = 80)
  overview  = models.TextField(blank=False, null=False)
  birthdate = models.DateField()
  country   = models.CharField(max_length=50)
  songs     = []
  state       = models.IntegerField()


class Album(models.Model):
  """
  DEFINES AN ALBUM
  """
  name        = models.CharField(max_length = 80)
  description = models.TextField(blank=False)
  genres      = []
  artist      = models.CharField(max_length=50)
  songs       = []
  state       = models.IntegerField()