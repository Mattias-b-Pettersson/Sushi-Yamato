from django.contrib.auth.models import Group, Permission, User
from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import get_object_or_404
from menu.models import (
    FoodItem,
    DrinkItem
)
import requests


class TestMenuViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.food_item_1 = FoodItem.objects.create(
            name="Meatballs",
            description="Meatballs and spaghetti",
            price="2.50",
            type="warm"
        )

        self.drink_item_1 = DrinkItem.objects.create(
            name="Cola",
            description="Cola Zero",
            price="2.50",
            type="cold"
        )
        self.food_filter = FoodItem.objects.all()
        self.drink_filter = DrinkItem.objects.all()

        # create permissions group
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        self.user.is_active = True
        self.user.save()

        # URLS
        self.menu_url = reverse('menu')
        self.edit_menu_item_url = reverse(
            "edit_menu_item", args=[self.food_filter.first().slug]
            )
        self.delete_food_item_url = reverse(
            "delete_food_item", args=[self.food_filter.first().slug]
            )
        self.delete_food_item_url = reverse(
            "delete_drink_item", args=[self.drink_filter.first().slug]
            )
        self.add_food_item_url = reverse("add_food_item")
        self.add_drink_item_url = reverse("add_drink_item")

    def test_menu_view_GET(self):
        """
        test if the menu page view is rendering successfully
        """
        response = self.client.get(self.menu_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "menu.html")

    