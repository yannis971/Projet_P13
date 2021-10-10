"""
Module : admin.py
Modified by : Yannis Saliniere
"""
from django.contrib import admin

from .models import Address, Letting, Profile

admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
