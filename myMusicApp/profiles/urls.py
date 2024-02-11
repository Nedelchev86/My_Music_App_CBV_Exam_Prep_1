
from django.contrib import admin
from django.urls import path

from myMusicApp.profiles.views import ProfileDetails, ProfileDelete

urlpatterns = [
    path("details/", ProfileDetails.as_view(), name="profile details"),
    path("delete/", ProfileDelete.as_view(), name="profile delete"),
]


