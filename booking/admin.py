from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    search_fields = ["firstname", "lastname", "date", "time"]
    list_display = ["firstname", "lastname", "date", "time"]
    list_filter = ("date",)
