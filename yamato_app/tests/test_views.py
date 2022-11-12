from django.contrib.auth.models import Group, Permission, User
from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import get_object_or_404
import requests


class TestYamatoViews(TestCase):

    def setUp(self):
        self.client = Client()

        # URLS
        self.home_url = reverse('home')
        self.contact_url = reverse("contact")

    def test_home_view_GET(self):
        """
        test if the home page view is rendering successfully
        """
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_contact_view_GET(self):
        """
        test if the contact page view is rendering successfully
        """
        response = self.client.get(self.contact_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")
