from django.shortcuts import render
from .models import My_Album

# Create your views here.


def albumpage(request):
    albums = My_Album.objects.all()
    context = {
        'albums': albums
    }
    return render(request, 'album/album.html', context)


def blueberry(request):

    context = {

    }
    return render(request, 'album/blueberry.html', context)
