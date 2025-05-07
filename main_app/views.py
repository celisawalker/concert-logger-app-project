from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from .models import Concert, Artist
from .tracks import get_songs_by_artist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect ('concert-index')
        else:
            error_message = 'Invalid login credentials - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

@login_required
def about(request):
    about_details = 'Take a walk down memory lane with your digital concert scrapbook. Relive The Eras Tour, Love on Tour and the Renaissance Tour all in one place.'
    return render(request, 'about.html', {
        'about': about_details
    })

@login_required
def concert_index(request):
    concerts = Concert.objects.filter(user=request.user)
    artists = Artist.objects.filter(user=request.user)

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

@login_required
def concert_detail(request, concert_id):
    concert = Concert.objects.get(id=concert_id)
    return render(request, 'concerts/detail.html', {
        'concert': concert
    })


class ConcertCreate(LoginRequiredMixin, CreateView):
    model = Concert
    fields = '__all__'
    success_url = '/concerts/'

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)
    

class ConcertUpdate(LoginRequiredMixin, UpdateView):
    model = Concert
    fields =  '__all__'

    success_url = '/concerts/'

class ConcertDelete(LoginRequiredMixin, DeleteView):
    model = Concert
    success_url = '/concerts/'

class ArtistCreate(LoginRequiredMixin, CreateView):
    model = Artist
    fields = '__all__'
    success_url = '/artists/'

class ArtistList(LoginRequiredMixin, ListView):
    model = Artist

    def get_queryset(self):
        user = self.request.user
        queryset = Artist.objects.filter(user=user)
        return queryset

class ArtistDetail(LoginRequiredMixin, DetailView):
    model = Artist

class ArtistUpdate(LoginRequiredMixin, UpdateView):
    model = Artist
    fields = ['name', 'genre']

class ArtistDelete(LoginRequiredMixin, DeleteView):
    model = Artist
    success_url = '/artists/'

