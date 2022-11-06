from django.urls import path, include
from menu import views

urlpatterns = [
    path("", views.MenuView.as_view(), name="menu"),
    path("delete_food_item/<slug>", views.DeleteFoodItem.as_view(), name="delete_food_item"),
    path("delete_drink_item/<slug>", views.DeleteDrinkItem.as_view(), name="delete_drink_item")
]