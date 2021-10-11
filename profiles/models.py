"""
Module : models.py
Created by : Yannis Saliniere
"""
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        String representation of a profile instance
        """
        return self.user.username
