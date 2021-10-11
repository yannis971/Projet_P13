"""
Module : test_views.py
Created by : Yannis Saliniere
"""
from django.test import TestCase
from django.urls import reverse
from lettings.models import Address, Letting


class LettingViewTest(TestCase):
    """
    Test of lettings app views
    """

    @classmethod
    def setUpTestData(cls):
        """
        Class method to set up the tests
        """
        cls.number_of_lettings = 12
        for letting_id in range(cls.number_of_lettings):
            address = Address.objects.create(
                number=(letting_id + 3260),
                street="Bedford Street",
                city="Brunswick",
                state="GA",
                zip_code=31525,
                country_iso_code="USA",
            )
            Letting.objects.create(
                title=f"Letting id {letting_id + 1}", address=address
            )

    def test_index_view(self):
        """
        Test index view
        """
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")
        self.assertEqual(
            len(response.context["lettings_list"]), self.number_of_lettings
        )

    def test_letting_view(self):
        """
        Test letting view
        """
        url = reverse("lettings:letting", kwargs={"letting_id": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/letting.html")
        self.assertEqual(response.context["title"], "Letting id 1")
        address = response.context["address"]
        self.assertEquals(address.number, 3260)
        self.assertEquals(address.street, "Bedford Street")
