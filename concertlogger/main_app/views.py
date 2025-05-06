from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .models import Concert, Artist
from .tracks import get_songs_by_artist
# Create your views here.

class Home(LoginView):
    template_name = 'home.html'


def about(request):
    about_details = 'Take a walk down memory lane with your digital concert scrapbook. Relive The Eras Tour, Love on Tour and the Renaissance Tour all in one place.'
    return render(request, 'about.html', {
        'about': about_details
    })

def concert_index(request):
    concerts = Concert.objects.all()
    artists = Artist.objects.all()

    def get_songs(artist_name):
        songs = []
        results = get_songs_by_artist(artist_name)

        for song in results:
            songs.append(song["name"])
        return songs
    
    for artist in artists:
        artist.top_songs = get_songs(artist.name)[:5]


    return render(request, 'concerts/index.html', {
        'concerts': concerts,
        'artists': artists,
        })

def concert_detail(request, concert_id):
    concert = Concert.objects.get(id=concert_id)
    return render(request, 'concerts/detail.html', {
        'concert': concert
    })

class ConcertCreate(CreateView):
    model = Concert
    fields = '__all__'
    success_url = '/concerts/'

    # def form_valid(self, form):
    #     # Assign the logged in user (self.request.user)
    #     form.instance.user = self.request.user  # form.instance is the cat
    #     # Let the CreateView do its job as usual
    #     return super().form_valid(form)

class ConcertUpdate(UpdateView):
    model = Concert
    fields =  '__all__'

    success_url = '/concerts/'

class ConcertDelete(DeleteView):
    model = Concert
    success_url = '/concerts/'

class ArtistCreate(CreateView):
    model = Artist
    fields = '__all__'
    success_url = '/artists/'

class ArtistList(ListView):
    model = Artist

class ArtistDetail(DetailView):
    model = Artist

class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['name', 'genre']

class ArtistDelete(DeleteView):
    model = Artist
    success_url = '/artists/'

