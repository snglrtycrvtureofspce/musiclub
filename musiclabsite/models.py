from django.db import models


class Author(models.Model):# Модель исполнителя.
    authorname = models.CharField(max_length=1000)

    def __str__(self):
        return self.authorname

class Album(models.Model):# Модель плейлиста.
    albumname = models.CharField(max_length=1000)
    author = models.ForeignKey('Author', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.albumname


class Song(models.Model):# Модель аудиозаписи.
    songname = models.CharField(max_length=1000)
    author = models.ForeignKey('Author', on_delete=models.DO_NOTHING)
    album = models.ForeignKey('Album', on_delete=models.DO_NOTHING)
    playlist = models.ForeignKey('Playlist', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.songname


class Playlist(models.Model):# Модель плейлиста.
    playlistname = models.CharField(max_length=1000)

    def __str__(self):
        return self.playlistname
