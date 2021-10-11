"""
Module : test_views.py
Created by : Yannis Saliniere
"""
from django.test import TestCase
from django.urls import reverse
from profiles.models import Profile, User


class ProfileViewTest(TestCase):
    """
    Test of profiles app views
    """

    @classmethod
    def setUpTestData(cls):
        """
        Class method to set up the tests
        """
        cls.favorite_cities = ["Paris", "London", "New-York", "Moscow", "Tokyo"]
        cls.number_of_profiles = 5
        for profile_id in range(cls.number_of_profiles):
            user = User.objects.create_user(
                username=f"username {profile_id}",
                password="Abc1234!",
                first_name=f"first_name {profile_id}",
                last_name=f"last_name {profile_id}",
                email=f"jonh.doe{profile_id}@example.com",
            )
            Profile.objects.create(
                favorite_city=cls.favorite_cities[profile_id], user=user
            )

    def test_index_view(self):
        """
        Test index view
        """
        response = self.client.get(reverse("profiles:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/index.html")
        self.assertEqual(
            len(response.context["profiles_list"]), self.number_of_profiles
        )

    def test_profile_view(self):
        """
        Test profile view
        """
        url = reverse("profiles:profile", kwargs={"username": "username 0"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
        profile = response.context["profile"]
        self.assertEquals(profile.favorite_city, self.favorite_cities[0])
        self.assertEquals(profile.user.username, "username 0")
