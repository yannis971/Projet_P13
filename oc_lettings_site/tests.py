"""
Module : tests.py
Modified by : Yannis Saliniere
"""

import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from .models import Address, Letting, Profile, User


@pytest.fixture
def create_letting(db):
    """
    Fixture to create a Letting instance
    """
    def make_letting(**kwargs):
        """
        Create an Address and returns a Letting instance
        """
        address = Address.objects.create(
            number=7217,
            street="Bedford Street",
            city="Brunswick",
            state="GA",
            zip_code=31525,
            country_iso_code="USA",
        )
        if 'title' not in kwargs:
            kwargs['title'] = "No title provided"
        kwargs['address'] = address
        return Letting.objects.create(**kwargs)

    return make_letting


@pytest.fixture
def create_profile(db):
    """
    Fixture to create a Profile instance
    """
    def make_profile(**kwargs):
        """
        Create a User and returns a Profile instance
        """
        user = User.objects.create_user(
            username=kwargs["username"],
            password="Abc1234!",
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
        )
        kwargs.pop("username")
        kwargs["user"] = user
        return Profile.objects.create(**kwargs)

    return make_profile


def test_dummy():
    """
    test_dummy
    """
    assert 1


@pytest.mark.django_db
@pytest.mark.parametrize(
    "url_name, template_name",
    [
        ("index", "index.html"),
        ("lettings_index", "lettings_index.html"),
        ("profiles_index", "profiles_index.html"),
    ],
)
def test_index_views(url_name, template_name, client):
    """
    Test index view
    """
    url = reverse(url_name)
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, template_name)


@pytest.mark.django_db
def test_letting_view(client, create_letting):
    """
    Test letting view
    """
    letting = create_letting(title="Joshua Tree Green Haus /w Hot Tub")
    url = reverse("letting", kwargs={"letting_id": letting.id})
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, "letting.html")


@pytest.mark.django_db
def test_profile_view(client, create_profile):
    """
    Test profile view
    """
    profile = create_profile(username="Darwin", favorite_city="Barcelona")
    url = reverse("profile", kwargs={"username": profile.user.username})
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, "profile.html")
