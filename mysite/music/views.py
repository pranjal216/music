from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Album

def index(request):
    all_Albums = Album.objects.all()
    context = {'all_Albums' : all_Albums}
    return render(request,'music/index.html', context)

def second_page(request):
    return HttpResponse( "This is second page")

def detail(request, album_id):
    album = get_object_or_404(Album,pk=album_id)
    return render(request,'music/detail.html', {'album' : album})

def favourite(request):
    return HttpResponse("this is not your favourite song")