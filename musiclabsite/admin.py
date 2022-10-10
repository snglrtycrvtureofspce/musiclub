from django.contrib import admin
from .models import Author, Album, Song, Playlist


admin.site.register(Author)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Playlist)
