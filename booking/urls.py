from django.urls import path, include
from booking import views

urlpatterns = [
    path("book-a-table/", views.BookingView.as_view(), name="book"),
    path("open-booking/", views.BookingEdit.as_view(), name="openbooking"),
    path("edit-booking/<booking_no>", views.BookingEditFilled.as_view(), name="editfilled"),
    path("delete-booking/<booking_no>", views.DeleteBooking.as_view(), name="delete"),
    path("show-bookings/", views.ShowAllBookings.as_view(), name="show"),
]