from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Booking
from .forms import BookingForm


# Create your views here.
def booking(request):
    form = BookingForm(request.POST)
    if request.method == "POST":
        if request.POST.get('booking-number', ''):
            booking_no = request.POST.get('booking-number', '')
            print(request.POST)
            if Booking.objects.filter(booking_no=booking_no).exists():
                if request.POST.get("action") == "viewbook":
                    print("retur§")
                    return redirect(f"view-booking/{booking_no}")
                elif request.POST.get("action") == "editbook":
                    print("retur")
                    return redirect(f"edit-booking/{booking_no}")
        if form.is_valid():
            form.save()
            return redirect("booking-confirmation")
    else:
        form = BookingForm()
        context = {
            "form": form
        }
        return render(request, "book.html", context)
