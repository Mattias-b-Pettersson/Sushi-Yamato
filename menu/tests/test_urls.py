from django.test import SimpleTestCase
from django.urls import reverse, resolve
from menu.views import (
    MenuView,
    DeleteFoodItem,
    DeleteDrinkItem,
    EditMenuItem,
    AddDrinkItem,
    AddFoodItem,
) 


class TestUrls(SimpleTestCase):
    def test_booking_url_is_resolved(self):
        url = reverse('menu')
        self.assertEquals(resolve(url).func.view_class, MenuView)
        
    def test__bookingsearch_url_is_resolved(self):
        url = reverse('delete_food_item', args=(["some-slug"]))
        self.assertEquals(resolve(url).func.view_class, DeleteFoodItem)

    def test__bookingedit_url_is_resolved(self):
        url = reverse('delete_drink_item', args=(["some-slug"]))
        self.assertEquals(resolve(url).func.view_class, DeleteDrinkItem)

    def test_deletebooking_url_is_resolved(self):
        url = reverse('edit_menu_item', args=(["some-slug"]))
        self.assertEquals(resolve(url).func.view_class, EditMenuItem)

    def test_show_all_booking_url_is_resolved(self):
        url = reverse('add_drink_item')
        self.assertEquals(resolve(url).func.view_class, AddDrinkItem)

    def test_checkbooking_url_is_resolved(self):
        url = reverse('add_food_item')
        self.assertEquals(resolve(url).func.view_class, AddFoodItem)
