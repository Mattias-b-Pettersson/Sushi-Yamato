from django.urls import path, include
from menu import views

urlpatterns = [
    path("", views.MenuView.as_view(), name="menu"),
    path("delete_food_item/<slug>", views.DeleteMenuItem.as_view(), name="delete_menu_item"),
    path("edit_menu_item/<slug>", views.EditMenuItem.as_view(), name="edit_menu_item"),
    path("add_menu_item", views.AddMenuItem.as_view(), name="add_menu_item"),
]