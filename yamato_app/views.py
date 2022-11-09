from django.shortcuts import render, get_object_or_404,  redirect
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages


class Home(View):
    def get(self, request):
        context = {
            "active": "home"
        }
        return render(request, "home.html", context)