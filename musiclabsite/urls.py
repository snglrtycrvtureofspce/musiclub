from django.urls import path
from musiclabsite.views import startpage, startpage2, mainmenu, albums, playlists, songs


urlpatterns = [
    path('sign_in', startpage, name='sign-in'),
    path('sign_up', startpage2, name='sign-up'),
    path('menu', mainmenu, name='menu'),
    path('albums', albums, name='albums'),
    path('playlists', playlists, name='playlists'),
    path('songs', songs, name='songs'),

]
