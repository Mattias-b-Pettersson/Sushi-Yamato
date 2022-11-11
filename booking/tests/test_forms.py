from django.test import TestCase
from ..forms import BookingForm


class TestBookingForm(TestCase):

    def test_booking_firstname_is_requierd(self):
        form = BookingForm({
            "firstname": "",
            "lastname": "testson",
            "phonenumber": "+46703150560",
            "email": "editedmail@mail.com",
            "date": "2022-2-9",
            "time": "11:00",
            "tablesize": "6",
            })
        self.assertFalse(form.is_valid())

    def test_booking_lastname_is_requierd(self):
        form = BookingForm({
            "firstname": "test",
            "lastname": "",
            "phonenumber": "+46703150560",
            "email": "editedmail@mail.com",
            "date": "2022-2-9",
            "time": "11:00",
            "tablesize": "6",
            })
        self.assertFalse(form.is_valid())

    def test_booking_email_is_requierd(self):
        form = BookingForm({
            "firstname": "test",
            "lastname": "testson",
            "phonenumber": "+46703150560",
            "email": "",
            "date": "2022-10-10",
            "time": "10:00",
            "tablesize": "6",
            })
        self.assertFalse(form.is_valid())

    def test_booking_date_is_requierd(self):
        form = BookingForm({
            "firstname": "test",
            "lastname": "testson",
            "phonenumber": "+46703150560",
            "email": "editedmail@mail.com",
            "date": "",
            "time": "10:00",
            "tablesize": "6",
            })
        self.assertFalse(form.is_valid())

    def test_booking_time_is_requierd(self):
        form = BookingForm({
            "firstname": "test",
            "lastname": "testson",
            "phonenumber": "+46703150560",
            "email": "editedmail@mail.com",
            "date": "2022-2-9",
            "time": "",
            "tablesize": "6",
            })
        self.assertFalse(form.is_valid())

    def test_booking_tablesize_is_requierd(self):
        form = BookingForm({
            "firstname": "test",
            "lastname": "testson",
            "phonenumber": "+46703150560",
            "email": "editedmail@mail.com",
            "date": "2022-2-9",
            "time": "10:00",
            "tablesize": "",
            })
        self.assertFalse(form.is_valid())

    def test_booking_phonenumber_is_not_requierd(self):
        form = BookingForm({
            "firstname": "test",
            "lastname": "testson",
            "phonenumber": "",
            "email": "editedmail@mail.com",
            "date": "2022-2-9",
            "time": "10:00",
            "tablesize": "2",
            })
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Make sure that all the fields are in form and is in the right order.
        """
        form = BookingForm()
        self.assertEqual(form.Meta.fields, (
            "firstname",
            "lastname",
            "email",
            "phonenumber",
            "date",
            "time",
            "tablesize"
            ))
