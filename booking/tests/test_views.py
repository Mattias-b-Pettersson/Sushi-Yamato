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
        self.booking_url = reverse('book')
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
        test if the booking page view is creating booking successfully
        """
        response = self.client.post(self.booking_url, {
            "firstname": "test7",
            "lastname": "testson",
            "phonenumber": "+46703150560",
            "email": "editedmail@mail.com",
            "date": "2022-2-9",
            "time": "11:00",
            "tablesize": "6",
            })
        booking_object = get_object_or_404(
            Booking, email="editedmail@mail.com"
            )
        self.assertEquals(
            len(Booking.objects.filter(firstname="test7")), 1
            )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "book.html")
        
        self.assertEquals(booking_object.firstname, "test7")
        self.assertEquals(booking_object.lastname, "testson")
        self.assertEquals(booking_object.phonenumber, "+46703150560")
        self.assertEquals(booking_object.email, "editedmail@mail.com")
        self.assertEquals(booking_object.date, datetime.date(2022, 2, 9))
        self.assertEquals(booking_object.time, "11:00")
        self.assertEquals(booking_object.tablesize, "6")

    def test_edit_booking_view_GET(self):
        """
        test if the edit booking page view is rendering successfully
        """
        response = self.client.get(self.edit_booking_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="edit-booking.html" and "base.html"
            )

    def test_edit_booking_view_POST(self):
        """
        test if the edit booking is accepting POST requests successfully
        """
        response = self.client.post(
            # Need to use hardcoded URL here because reverse
            # don't accept all the variables
            f"/booking/edit/{Booking.objects.first()}",
            {
             "firstname": "test9",
             "lastname": "testson",
             "phonenumber": "+46703150560",
             "email": "editedmail@mail.com",
             "date": "2022-2-9",
             "time": "11:00",
             "tablesize": "6",
            }
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="edit-booking.html" and "base.html"
            )
        booking_object = get_object_or_404(
            Booking, booking_no=Booking.objects.first()
            )
        self.assertEquals(booking_object.firstname, "test9")
        self.assertEquals(booking_object.lastname, "testson")
        self.assertEquals(booking_object.phonenumber, "+46703150560")
        self.assertEquals(booking_object.email, "editedmail@mail.com")
        self.assertEquals(booking_object.date, datetime.date(2022, 2, 9))
        self.assertEquals(booking_object.time, "11:00")
        self.assertEquals(booking_object.tablesize, "6")

    def test_delete_booking_view_GET(self):
        """
        test if the delete booking view is deleting booking
        and successfully redirects
        """
        self.booking_filter
        response = self.client.get(self.delete_bookings_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(len(self.booking_filter), 0)

    def test_check_bookings_view_api_GET(self):
        """
        check if the right response are sent back from the API function
        for the JS running on booking page
        """
        # check if the right response are
        # sent back and the form has not been touched.
        response = self.client.get(self.check_bookings_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()["tableAvailable"], True)

        # check if the right response are
        # sent back and there is a table available.
        response2 = self.client.get(self.check_bookings_url, {
                                    "date": "2022-11-10",
                                    "time": "11:00",
                                    "tablesize": 2
                                    })
        self.assertEquals(response2.json()["tableAvailable"], True)

        # check if the right response are
        # sent back there is no table available.
        response3 = self.client.get(self.check_bookings_url, {
                                    "date": "2022-11-10",
                                    "time": "10:00",
                                    "tablesize": 2
                                    })
        self.assertEquals(response3.json()["tableAvailable"], False)
