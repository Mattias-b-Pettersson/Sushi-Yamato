from django.test import SimpleTestCase
from django.urls import reverse, resolve
from menu.views import (
    MenuView,
    DeleteMenuItem,
    EditMenuItem,
    AddMenuItem,
)


class TestUrls(SimpleTestCase):
    def test_menu_url_is_resolved(self):
        url = reverse('menu')
        self.assertEquals(resolve(url).func.view_class, MenuView)
        
    def test__delete_menu_item_url_is_resolved(self):
        url = reverse('delete_menu_item', args=(["some-slug"]))
        self.assertEquals(resolve(url).func.view_class, DeleteMenuItem)

    def test_edit_menu_item_url_is_resolved(self):
        url = reverse('edit_menu_item', args=(["some-slug"]))
        self.assertEquals(resolve(url).func.view_class, EditMenuItem)

    def test_add_menu_item_url_is_resolved(self):
        url = reverse('add_menu_item')
        self.assertEquals(resolve(url).func.view_class, AddMenuItem)
