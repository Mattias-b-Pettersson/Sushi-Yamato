from django.test import SimpleTestCase
from django.urls import reverse, resolve
from yamato_app.views import Home, Contact


class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, Home)

    def test_Contact_url_is_resolved(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func.view_class, Contact)
