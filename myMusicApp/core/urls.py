
from django.contrib import admin
from django.urls import path

from myMusicApp.profiles.views import HomePageView, HomePageNoProfile

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path('create-profile/', HomePageNoProfile.as_view(), name='create_profile'),
]
