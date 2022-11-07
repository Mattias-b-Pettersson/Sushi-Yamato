from django.urls import path, include
from menu import views

urlpatterns = [
    path("", views.MenuView.as_view(), name="menu"),
    path("delete_food_item/<slug>", views.DeleteFoodItem.as_view(), name="delete_food_item"),
    path("delete_drink_item/<slug>", views.DeleteDrinkItem.as_view(), name="delete_drink_item"),
    path("edit_menu_item/<slug>", views.EditMenuItem.as_view(), name="edit_menu_item"),
    path("add_drink_item", views.AddDrinkItem.as_view(), name="add_drink_item"),
    path("add_food_item", views.AddFoodItem.as_view(), name="add_food_item"),

]