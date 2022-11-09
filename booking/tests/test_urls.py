from django.test import SimpleTestCase
from django.urls import reverse, resolve
from booking.views import (BookingView, BookingSearch,
                           BookingEdit, DeleteBooking,
                           ShowAllBookings, CheckBookings)


class TestUrls(SimpleTestCase):
    def test_booking_url_is_resolved(self):
        url = reverse('book')
        self.assertEquals(resolve(url).func.view_class, BookingView)
        
    def test__bookingsearch_url_is_resolved(self):
        url = reverse('open_booking')
        self.assertEquals(resolve(url).func.view_class, BookingSearch)

    def test__bookingedit_url_is_resolved(self):
        url = reverse('edit_booking', args=(["booking_no"]))
        self.assertEquals(resolve(url).func.view_class, BookingEdit)

    def test_deletebooking_url_is_resolved(self):
        url = reverse('delete_booking', args=(["booking_no"]))
        self.assertEquals(resolve(url).func.view_class, DeleteBooking)

    def test_show_all_booking_url_is_resolved(self):
        url = reverse('all_bookings')
        self.assertEquals(resolve(url).func.view_class, ShowAllBookings)

    def test_checkbooking_url_is_resolved(self):
        url = reverse('check_bookings')
        self.assertEquals(resolve(url).func.view_class, CheckBookings)
