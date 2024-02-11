from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from myMusicApp.albums.models import Album
from myMusicApp.profiles.models import Profile


# Create your views here.


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


class HomePageView(views.TemplateView):
    def get(self, request, *args, **kwargs):
        profile = get_profile()

        if profile is None:
            return HomePageNoProfile.as_view()(request)
        return HomePageWithProfile.as_view()(request)






class HomePageNoProfile(views.CreateView):
    template_name = "home-no-profile.html"
    model = Profile
    success_url = "/"
    fields = "__all__"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs['placeholder'] = 'Username'
        form.fields['email'].widget.attrs['placeholder'] = 'Email'
        form.fields['age'].widget.attrs['placeholder'] = 'Age'
        return form




class HomePageWithProfile(views.ListView):
    template_name = "home-with-profile.html"
    model = Album
    print(get_profile())
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['have_profile'] = get_profile()
        return context



class ProfileDetails(views.DetailView):
    model = Profile
    fields = "__all__"
    success_url = "/"
    template_name = "profile-details.html"

    def get_object(self, queryset=None):
        return Profile.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["albums"] = Album.objects.all().count()
        context['have_profile'] = get_profile()
        return context


class ProfileDelete(views.DeleteView):
    model = Profile
    template_name = "profile-delete.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return Profile.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['have_profile'] = get_profile()
        return context
