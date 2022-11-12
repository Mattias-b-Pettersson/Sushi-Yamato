from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    search_fields = ["firstname", "lastname", "date", "time", "booking_no", ]
    list_display = ["booking_no", "firstname", "lastname", "date", "time", ]
    list_filter = ("date",)
