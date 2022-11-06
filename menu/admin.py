from django.contrib import admin
from .models import DrinkItem, FoodItem


@admin.register(FoodItem)
class FoodAdmin(admin.ModelAdmin):
    search_fields = ["name", "price", "type", "description"]
    list_display = ["name", "price", "type", "description"]
    list_filter = ("name", "price", "type")

@admin.register(DrinkItem)
class DrinkAdmin(admin.ModelAdmin):
    search_fields = ["name", "price", "type", "description"]
    list_display = ["name", "price", "type", "description"]
    list_filter = ("type",)