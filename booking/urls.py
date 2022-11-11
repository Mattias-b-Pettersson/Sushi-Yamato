from django.urls import path, include
from booking import views

urlpatterns = [
    path("", views.BookingView.as_view(), name="book"),
    path("open/", views.BookingSearch.as_view(), name="open_booking"),
    path("edit/<booking_no>",
         views.BookingEdit.as_view(),
         name="edit_booking"
         ),
    path("delete/<booking_no>",
         views.DeleteBooking.as_view(),
         name="delete_booking"
         ),
    path("all/", views.ShowAllBookings.as_view(), name="all_bookings"),
    path("check/", views.CheckBookings.as_view(), name="check_bookings"),
]
