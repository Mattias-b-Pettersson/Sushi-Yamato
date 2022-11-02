from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


class Home(View):
    def get(self, request):
        form = BookingForm()
        context = {
            "active": "home"
        }
        return render(request, "home.html", context)

class BookingView(View):
    def post(self, request):
        form = BookingForm(request.POST)
        if request.POST.get("booking-number"):
            booking_no = request.POST.get("booking-number")
            print(Booking.objects)
            if Booking.objects.filter(booking_no=booking_no).exists():
                if request.POST.get("action") == "viewbook":
                    return redirect(f"view-booking/{booking_no}")
                elif request.POST.get("action") == "editbook":
                    return redirect(f"edit-booking/{booking_no}")

        if form.is_valid():
            print(form.is_valid())
            booking = form.save()
            messages.success(request, f"Booking with bookingnumber {booking} is a success!")
            context = {
                "form": form,
            }

            return render(request, "book.html", context)
        elif form.is_valid() != True:
            context = {
                
                "form": form
            }
            messages.error(request, f"Booking failed!")
            return render(request, "book.html", context)

    def get(self, request):
        form = BookingForm()
        context = {
            "form": form,
            "active": "home"
        }
        return render(request, "book.html", context)



# def booking(request):
#     
#     if request.method == "POST":
#         if request.POST.get('booking-number', ''):
#             booking_no = request.POST.get('booking-number', '')
#             print(request.POST)
#             if Booking.objects.filter(booking_no=booking_no).exists():
#                 if request.POST.get("action") == "viewbook":
#                     print("retur§")
#                     return redirect(f"view-booking/{booking_no}")
#                 elif request.POST.get("action") == "editbook":
#                     print("retur")
#                     return redirect(f"edit-booking/{booking_no}")
#         if form.is_valid():
#             form.save()
#             return redirect("booking-confirmation")
#     else:
#         form = BookingForm()
#         context = {
#             "form": form
#         }
#         return render(request, "book.html", context)


class BookingEdit(View):
    def post(self, request, booking_no):
        bookingitem = get_object_or_404(Booking, booking_no=booking_no)
        if request.method == "POST":
            form = BookingForm(request.POST, instance=bookingitem)
            if request.POST.get("action") == "delete":
                bookingitem.delete()
                return redirect("/")
            if form.is_valid():
                form.save()
                return redirect("/")

    def get(self, request, booking_no):
        bookingitem = get_object_or_404(Booking, booking_no=booking_no)
        filledform = BookingForm(instance=bookingitem)
        context = {
            "form": filledform
        }
        return render(request, "edit-booking.html", context)


class DeleteBooking(View):
    def get(selft, request, booking_no):
        bookingitem = get_object_or_404(Booking, booking_no=booking_no)
        bookingitem.delete()
        return redirect("")


class ShowBooking(View):
    def get(self, request, booking_no):
        bookingitem = get_object_or_404(Booking, booking_no=booking_no)
        context = {
                "bookingitem": bookingitem
            }
        return render(request, "view-booking.html", context)