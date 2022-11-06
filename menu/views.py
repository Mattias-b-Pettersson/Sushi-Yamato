from django.shortcuts import render, get_object_or_404,  redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import FoodItem, DrinkItem 


class MenuView(View):
    def get(self, request):

        warm_drink_items = DrinkItem.objects.filter(type="warm")
        cold_drink_items = DrinkItem.objects.filter(type="cold")
        beer_drink_items = DrinkItem.objects.filter(type="beer")
        wine_drink_items = DrinkItem.objects.filter(type="wine")
        sake_drink_items = DrinkItem.objects.filter(type="sake")
        sushi_food_items = FoodItem.objects.filter(type="sushi")
        rolls_food_items = FoodItem.objects.filter(type="rolls")
        bowl_food_items = FoodItem.objects.filter(type="bowls")
        warm_food_items = FoodItem.objects.filter(type="warm")
        context = {
            "active": "menu",
            "warm_drink_items": warm_drink_items,
            "cold_drink_items" : cold_drink_items,
            "beer_drink_items" : beer_drink_items,
            "wine_drink_items" : wine_drink_items,
            "sake_drink_items" : sake_drink_items,
            "sushi_food_items" : sushi_food_items,
            "rolls_food_items" : rolls_food_items,
            "bowl_food_items" : bowl_food_items,
            "warm_food_items" : warm_food_items,
        }

        return render(request, "menu.html", context)


class DeleteFoodItem(View):
    def get(self, request, slug):
        food_item = get_object_or_404(FoodItem, slug=slug)
        food_item.delete()
        messages.success(request, "Menu item deleted!")
        return redirect(reverse("menu"))

class DeleteDrinkItem(View):
    def get(self, request, slug):
        drink_item = get_object_or_404(DrinkItem, slug=slug)
        drink_item.delete()
        messages.success(request, "Menu item deleted!")
        return redirect(reverse("menu"))

