from django.urls import path, include
from yamato_app import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
]