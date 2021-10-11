"""
Module : views.py
Created by : Yannis Saliniere
"""
from django.shortcuts import render
from .models import Letting


def index(request):
    """
    lettings_index view
    :param request:
    :return: template index.html
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    letting view
    :param request:
    :param letting_id: the id of the letting retrieved
    :return: template letting.html
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
