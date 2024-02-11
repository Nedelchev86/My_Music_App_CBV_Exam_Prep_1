from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from myMusicApp.albums.forms import DeleteAlbumForm
from myMusicApp.albums.models import Album
from myMusicApp.profiles.models import Profile
from myMusicApp.profiles.views import get_profile


# Create your views here.


class AddAlbum(views.CreateView):
    model = Album
    template_name = "album-add.html"
    fields = ["album_name", "artist", "genre", "description", "image_url", "price",]
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['have_profile'] = get_profile()
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['album_name'].label = 'Album Name'
        form.fields['image_url'].label = 'Image URL'

        form.fields['album_name'].widget.attrs['placeholder'] = 'Album Name'
        form.fields['artist'].widget.attrs['placeholder'] = 'Artist'
        form.fields['description'].widget.attrs['placeholder'] = 'Description'
        form.fields['image_url'].widget.attrs['placeholder'] = 'Image URL'
        form.fields['price'].widget.attrs['placeholder'] = 'Price'
        # Change labels for other fields as needed
        return form

    def form_valid(self, form):
        form.instance.owner = Profile.objects.first()
        return super().form_valid(form)


class AlbumDetails(views.DetailView):
    model = Album
    template_name = 'album-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['have_profile'] = get_profile()
        return context


class EditAlbum(views.UpdateView):
    model = Album
    fields = ["album_name", "artist", "genre", "description", "image_url", "price",]
    template_name = "album-edit.html"
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['have_profile'] = get_profile()
        return context

class DeleteAlbum(views.DeleteView):
    model = Album
    template_name = "album-delete.html"
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DeleteAlbumForm(instance=self.get_object())
        context['have_profile'] = get_profile()

        return context

    def form_valid(self, form):
        Album.objects.all().delete()
        return super().form_valid(form)




