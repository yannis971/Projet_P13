"""
Module : views.py
Created by : Yannis Saliniere
"""
from django.shortcuts import render

from .models import Profile


def index(request):
    """
    lettings_index view
    :param request:
    :return: template profiles_index.html
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    profile view
    :param request:
    :param username: the username of the profile retrieved
    :return: template profile.html
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
