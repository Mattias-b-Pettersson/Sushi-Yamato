from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    search_fields = ["name", "price", "type", "description"]
    list_display = ["name", "price", "type", "description"]
    list_filter = ("name", "price", "type")