from django.contrib.auth.models import Group, Permission, User
from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import get_object_or_404
from menu.models import (
    MenuItem,

)
import requests


class TestMenuViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.menu_item_1 = MenuItem.objects.create(
            name="Meatballs",
            description="Meatballs and spaghetti",
            price="2.50",
            type="warm"
        )

        self.menu_filter = MenuItem.objects.all()


        # create permissions group
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        self.user.is_active = True
        self.user.save()

        # URLS
        self.menu_url = reverse('menu')
        self.edit_menu_item_url = reverse(
            "edit_menu_item", args=[self.menu_filter.first().slug]
            )
        self.delete_menu_item_url = reverse(
            "delete_menu_item", args=[self.menu_filter.first().slug]
            )
        self.add_menu_item_url = reverse("add_menu_item")

    def test_menu_view_GET(self):
        """
        test if the menu page view is rendering successfully
        """
        response = self.client.get(self.menu_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "menu.html")

    def test_delete_menu_item_no_access_GET(self):
        """
        Test if permission is denied without permission
        """

        # test access with out permission
        response = self.client.get(reverse(
            "delete_menu_item", args=[self.menu_filter.all()[0].slug]
            ))
        self.assertEquals(response.status_code, 302)
        self.assertEqual(len(self.menu_filter), 1)


    def test_delete_menu_item_with_access_GET(self):
        """
        Test if user can access delete function with right permission
        """
        delete_menuitem = Permission.objects.get(codename="delete_menuitem")

        # Add the permissions needed and log in.
        self.user.user_permissions.add(delete_menuitem)
        self.client.login(username='test', password='test')
        # Double checks that the user is logged in
        self.assertEqual(
            int(self.client.session['_auth_user_id']), self.user.pk)

        response = self.client.get(reverse(
            "delete_menu_item", args=[self.menu_filter.all()[0].slug]
            ))
        self.assertEqual(len(self.menu_filter), 0)
        self.assertEquals(response.status_code, 302)

    def test_add_menu_item_GET(self):
        """
        test if the add menu view is rendering successfully
        """
        response = self.client.get(self.add_menu_item_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "add-menu-item.html")

    def test_add_menu_item_POST(self):
        """
        test if the page adds menu item successfully
        """
        response = self.client.post(self.add_menu_item_url, {
            "name": "sashimi",
            "description": "Meatballs and spaghetti",
            "price": "300",
            "type": "warm food"
            })
        menu_object = get_object_or_404(
            MenuItem, name="sashimi"
            )
        self.assertEquals(
            len(MenuItem.objects.filter(name="sashimi")), 1
            )
        self.assertEquals(response.status_code, 302)
        self.assertEquals(menu_object.name, "sashimi")
        self.assertEquals(menu_object.description, "Meatballs and spaghetti")
        self.assertEquals(menu_object.price, "300")
        self.assertEquals(menu_object.type, "warm food")