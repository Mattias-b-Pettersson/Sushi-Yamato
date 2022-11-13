from django.shortcuts import render, get_object_or_404,  redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from .models import MenuItem
from .forms import MenuItemForm


class MenuView(View):
    """
    Displays the menu with all the menu items
    """
    def get(self, request):

        warm_drink_items = MenuItem.objects.filter(type="warm beverage")
        cold_drink_items = MenuItem.objects.filter(type="cold beverage")
        beer_drink_items = MenuItem.objects.filter(type="beer")
        wine_drink_items = MenuItem.objects.filter(type="wine")
        sake_drink_items = MenuItem.objects.filter(type="sake")
        sushi_food_items = MenuItem.objects.filter(type="sushi")
        rolls_food_items = MenuItem.objects.filter(type="rolls")
        bowl_food_items = MenuItem.objects.filter(type="bowls")
        warm_food_items = MenuItem.objects.filter(type="warm food")
        context = {
            "active": "menu",
            "warm_drink_items": warm_drink_items,
            "cold_drink_items": cold_drink_items,
            "beer_drink_items": beer_drink_items,
            "wine_drink_items": wine_drink_items,
            "sake_drink_items": sake_drink_items,
            "sushi_food_items": sushi_food_items,
            "rolls_food_items": rolls_food_items,
            "bowl_food_items": bowl_food_items,
            "warm_food_items": warm_food_items,
        }

        return render(request, "menu.html", context)


class DeleteMenuItem(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    Removes the menu item if it is found, then redirects back to the menu
    """
    permission_required = (
        "menu.delete_menuitem",
        )

    def get(self, request, slug):
        menu_item = get_object_or_404(MenuItem, slug=slug)
        menu_item.delete()
        messages.success(request, "Menu item deleted!")
        return redirect(reverse("menu"))


class EditMenuItem(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    Possible to edit the edit menu item if the right slug is passed in the the view
    """

    login_url = "/accounts/login/"
    permission_required = (
        "menu.change_menuitem",
        )

    def post(self, request, slug):
        if MenuItem.objects.filter(slug=slug).exists():
            menu_item = get_object_or_404(MenuItem, slug=slug)
            form = MenuItemForm(request.POST, instance=menu_item)
            filledform = MenuItemForm(instance=menu_item)
            context = {
                    "active": "menu",
                    "form": filledform,
                }

            if form.is_valid():
                form.save()
                messages.success(request, "Update successfull!")
                return redirect(reverse("menu"))

            if not form.is_valid():
                messages.error(request, "Update was not successfull!")
                return render(request, "edit-menu.html", context)

        else:
            messages.error(request, "Menu item was not found!")
            return redirect(reverse("menu"))

    def get(self, request, slug):
        if MenuItem.objects.filter(slug=slug).exists():
            drink_item = get_object_or_404(MenuItem, slug=slug)
            drink_form = MenuItemForm(instance=drink_item)
            context = {
                "active": "menu",
                "form": drink_form,
            }
            return render(request, "edit-menu.html", context)

        else:
            messages.error(request, "Menu item was not found!")
            return redirect(reverse("menu"))


class AddMenuItem(View):
    """
    Adds menu items to the menu if the form is valid
    """
    def post(self, request):
        form = MenuItemForm(request.POST)
        if form.is_valid():
            context = {
                    "form": form,
                }
            menu_item = form.save()
            messages.success(
                request,
                f"Menu item {menu_item.name} is created!"
                )
            return redirect(reverse("menu"))
        else:
            context = {
                "form": form
            }
            messages.warning(request, f"Menu item creation failed!")
            return render(request, "add-menu-item.html", context)

    def get(self, request):
        form = MenuItemForm
        context = {
            "form": form,
            "active": "menu"
        }
        return render(request, "add-menu-item.html", context)
