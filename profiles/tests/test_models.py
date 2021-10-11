"""
Module : test_models.py
Created by : Yannis Saliniere
"""
from django.test import TestCase
from profiles.models import Profile, User


class ProfileModelTest(TestCase):
    """
    Test of model Profile
    """

    @classmethod
    def setUpTestData(cls):
        """
        Class method to set up the tests
        """
        user = User.objects.create_user(
            username="DarwinTest",
            password="Abc1234!",
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
        )
        cls.profile = Profile.objects.create(favorite_city="Barcelona", user=user)

    def test_str(self):
        """
        Verify '__str__()' method
        """
        self.assertEquals(str(self.profile), "DarwinTest")

    def test_verbose_name(self):
        """
        Verify 'verbose_name' and 'verbose_name_plural' attributes
        """
        self.assertEquals(self.profile._meta.verbose_name, "profile")
        self.assertEquals(self.profile._meta.verbose_name_plural, "profiles")

    def test_count(self):
        """
        Verify 'count()' method
        """
        self.assertEquals(Profile.objects.count(), 1)
