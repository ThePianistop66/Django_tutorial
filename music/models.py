from __future__ import unicode_literals
from django.db import models

class Album(models.Model):
    album_title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    year = models.IntegerField(max_length=4)
    genre= models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    song_title = models.CharField(max_length=100)
    file_type= models.CharField(max_length=4)

    def __str__(self):
        return self.song_title