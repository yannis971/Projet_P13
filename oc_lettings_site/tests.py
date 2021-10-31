"""
Module : tests.py
Modified by : Yannis Saliniere
"""

import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_dummy():
    """
    test_dummy
    """
    assert 1


@pytest.mark.django_db
@pytest.mark.parametrize(
    "url_name, template_name",
    [
        ("oc_lettings_site:index", "oc_lettings_site/index.html"),
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
    assert b"<title>Holiday Homes</title>" in response.content
