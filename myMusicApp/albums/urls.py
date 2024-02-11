
from django.contrib import admin
from django.urls import path

from myMusicApp.albums.views import AddAlbum, AlbumDetails, EditAlbum, DeleteAlbum


urlpatterns = [
    path("add/", AddAlbum.as_view(), name="add album"),
    path("<int:pk>/details/", AlbumDetails.as_view(), name="album details"),
    path("<int:pk>/edit/", EditAlbum.as_view(), name="edit album"),
    path("<int:pk>/delete/", DeleteAlbum.as_view(), name="delete album"),
]



