from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import get_object_or_404
from booking.models import Booking
import datetime
import requests


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        # Needs 4 bookings to test the function that
        # looks if there are no available tables,
        # and one extra to see if there are available tables
        self.booking_1 = Booking.objects.create(
            firstname="test",
            lastname="testson",
            date="2022-11-10",
            time="10:00",
            tablesize=2
        )
        self.booking_2 = Booking.objects.create(
            firstname="test2",
            lastname="testson2",
            date="2022-11-10",
            time="10:00",
            tablesize=2
        )
        self.booking_3 = Booking.objects.create(
            firstname="test3",
            lastname="testson3",
            date="2022-11-10",
            time="10:00",
            tablesize=2
        )
        self.booking_4 = Booking.objects.create(
            firstname="test4",
            lastname="testson",
            date="2022-11-10",
            time="10:00",
            tablesize=2
        )
        self.booking_5 = Booking.objects.create(
            firstname="test5",
            lastname="testson",
            date="2022-11-10",
            time="11:00",
            tablesize=2
        )

        self.booking_filter = Booking.objects.filter(
            firstname="test", lastname="testson"
            )

        # URLS
        self.booking_url = reverse("book")
        self.open_booking_url = reverse("open_booking")
        self.edit_booking_url = reverse("edit_booking",
                                        args=([self.booking_filter[0]]))
        self.check_bookings_url = reverse("check_bookings")
        self.delete_bookings_url = reverse("delete_booking",
                                           args=([self.booking_filter[0]]))

    def test_book_view_GET(self):
        """
        test if the booking page view is rendering successfully
        """
        response = self.client.get(self.booking_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "book.html")

    def test_book_view_POST(self):
        """
        test if the booking page view is accepting POST requests successfully
        """
        response = self.client.post(self.booking_url, {
            "firstname": "test7",
            "lastname": "testson",
            "phonenumber": "+46703150560",
            "email": "mail@mail.com",
            "date": "2022-11-9",
            "time": "11:00",
            "tablesize": "2",
            })
        self.assertEquals(
            len(Booking.objects.filter(firstname="test7")), 1
            )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "book.html")