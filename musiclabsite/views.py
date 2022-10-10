from django.shortcuts import render



def startpage(request):# Страница авторизации.
    return render(request, 'musiclabsite/startpage.html')

def startpage2(request):# Страница регистрации.
    return render(request, 'musiclabsite/startpage2.html')

def mainmenu(request):# Страница исполнтелей(стартовая).
    return render(request, 'musiclabsite/mainmenu.html')

def albums(request):# Страница альбомов.
    return render(request, 'musiclabsite/albums.html')

def playlists(request):# Страница плейлистов.
    return render(request, 'musiclabsite/playlists.html')

def songs(request):# Страница треков.
    return render(request, 'musiclabsite/songs.html')
