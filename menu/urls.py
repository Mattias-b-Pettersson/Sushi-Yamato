from django.urls import path, include
from menu import views

urlpatterns = [
    path("", views.MenuView.as_view(), name="menu"),
    
]