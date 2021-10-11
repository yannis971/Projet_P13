"""
Module : test_models.py
Created by : Yannis Saliniere
"""
from django.test import TestCase
from lettings.models import Address, Letting


class AddressModelTest(TestCase):
    """
    Tests of model Address
    """

    @classmethod
    def setUpTestData(cls):
        """
        Class method to set up the tests
        """
        cls.address = Address.objects.create(
            number=7217,
            street="Bedford Street",
            city="Brunswick",
            state="GA",
            zip_code=31525,
            country_iso_code="USA",
        )

    def test_str(self):
        """
        Verify '__str__()' method
        """
        self.assertEquals(str(self.address), "7217 Bedford Street")

    def test_verbose_name(self):
        """
        Verify 'verbose_name' and 'verbose_name_plural' attributes
        """
        self.assertEquals(self.address._meta.verbose_name, "address")
        self.assertEquals(self.address._meta.verbose_name_plural, "addresses")

    def test_count(self):
        """
        Verify 'count()' method
        """
        self.assertEquals(Address.objects.count(), 1)


class LettingModelTest(TestCase):
    """
    Test of model Letting
    """

    @classmethod
    def setUpTestData(cls):
        """
        Class method to set up the tests
        """
        address = Address.objects.create(
            number=7217,
            street="Bedford Street",
            city="Brunswick",
            state="GA",
            zip_code=31525,
            country_iso_code="USA",
        )

        cls.letting = Letting.objects.create(
            title="Joshua Tree Green Haus /w Hot Tub", address=address
        )

    def test_str(self):
        """
        Verify '__str__()' method
        """
        self.assertEquals(str(self.letting), "Joshua Tree Green Haus /w Hot Tub")

    def test_verbose_name(self):
        """
        Verify 'verbose_name' and 'verbose_name_plural' attributes
        """
        self.assertEquals(self.letting._meta.verbose_name, "letting")
        self.assertEquals(self.letting._meta.verbose_name_plural, "lettings")

    def test_count(self):
        """
        Verify 'count()' method
        """
        self.assertEquals(Letting.objects.count(), 1)
