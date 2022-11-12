from django.test import TestCase
from ..forms import MenuItemForm



class TestMenuForm(TestCase):

    def test_menu_form_name_is_requierd(self):
        form = MenuItemForm({
            "name": "",
            "description": "Hello",
            "price": "3.50",
            "type": "warm food",
            })
        self.assertFalse(form.is_valid())

    def test_menu_form_description_is_requierd(self):
        form = MenuItemForm({
            "name": "hello",
            "description": "",
            "price": "3.50",
            "type": "warm food",
            })
        self.assertFalse(form.is_valid())

    def test_menu_form_price_is_requierd(self):
        form = MenuItemForm({
            "name": "hello",
            "description": "hello description",
            "price": "",
            "type": "warm food",
            })
        self.assertFalse(form.is_valid())

    def test_menu_form_type_is_requierd(self):
        form = MenuItemForm({
            "name": "hello",
            "description": "hello description",
            "price": "3.50",
            "type": "",
            })
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Make sure that all the fields are in form and is in the right order.
        """
        form = MenuItemForm()
        self.assertEqual(form.Meta.fields, (
            "name",
            "description",
            "price",
            "type",
            ))
