from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm

class MusicianListView(ListView):
    model = Musician

class MusicianDetailView(DetailView):
    model = Musician

class MusicianCreateView(CreateView):
    model = Musician
    form_class = MusicianForm
    success_url = reverse_lazy('musician_list')

class MusicianUpdateView(UpdateView):
    model = Musician
    form_class = MusicianForm
    success_url = reverse_lazy('musician_list')

class MusicianDeleteView(DeleteView):
    model = Musician
    success_url = reverse_lazy('musician_list')

class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy('musician_list')

class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy('musician_list')

class AlbumDeleteView(DeleteView):
    model = Album
    success_url = reverse_lazy('musician_list')
