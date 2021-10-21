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

    def test_index_view_is_accessible_by_name(self):
        """
        Test index view is accessible by name
        """
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        """
        Test index view url uses correct template
        """
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")

    def test_index_view_has_correct_title(self):
        """
        Test index view url has correct title
        """
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<title>Lettings</title>", response.content)

    def test_index_view_returns_correct_number_of_lettings(self):
        """
        Test index view url uses correct template
        """
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.context["lettings_list"]), self.number_of_lettings
        )

    def test_letting_view_is_accessible_by_name(self):
        """
        Test letting view is accessible by name
        """
        url = reverse("lettings:letting", kwargs={"letting_id": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_letting_view_uses_correct_template(self):
        """
        Test letting view uses correct template
        """
        url = reverse("lettings:letting", kwargs={"letting_id": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/letting.html")

    def test_letting_view_has_correct_title(self):
        """
        Test letting view has correct title
        """
        url = reverse("lettings:letting", kwargs={"letting_id": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<title>Letting id 1</title>", response.content)
        self.assertEqual(response.context["title"], "Letting id 1")
        address = response.context["address"]
        self.assertEquals(address.number, 3260)
        self.assertEquals(address.street, "Bedford Street")

    def test_letting_view_returns_correct_data(self):
        """
        Test letting view returns correct data
        """
        url = reverse("lettings:letting", kwargs={"letting_id": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "Letting id 1")
        address = response.context["address"]
        self.assertEquals(address.number, 3260)
        self.assertEquals(address.street, "Bedford Street")
        self.assertEquals(address.city, "Brunswick")
        self.assertEquals(address.state, "GA")
        self.assertEquals(address.country_iso_code, "USA")
