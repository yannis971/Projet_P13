"""
Module : views.py
Modified by : Yannis Saliniere
"""
from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo conse
# ctetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis, sem mi convallis ero
# s, vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget consequat ipsum lobo
# rtis quis. Phasellus eleifend ex auctor venenatis tempus.Aliquam vitae erat ac orci placerat luct
# us. Nullam elementum urna nisi, pellentesque iaculis enim cursus in. Praesent volutpat porttitor
# magna, non finibus neque cursus id.
def index(request):
    """
    index view
    :param request:
    :return: template index.html
    """
    return render(request, "index.html")
