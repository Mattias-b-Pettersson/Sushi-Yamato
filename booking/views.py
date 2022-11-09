from django.shortcuts import render, get_object_or_404,  redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Booking
from .forms import BookingForm


class BookingView(View):
    def post(self, request):
        form = BookingForm(request.POST)
        booking_date = request.POST.get("date")
        booking_time = request.POST.get("time")
        booking_tablesize = request.POST.get("tablesize")
        if form.is_valid():
            print(form.is_valid())
            context = {
                    "form": form,
                }
            if len(Booking.objects.filter(time=booking_time, date=booking_date, tablesize=booking_tablesize)) > 3:
                messages.warning(request, "Sorry. Can't make a booking at this time, not enough tables available.")
                return render(request, "book.html", context)
            else:
                booking = form.save()
                messages.success(request, f"Booking with bookingnumber {booking} is a success!")
            return render(request, "book.html", context)
        elif form.is_valid() != True:
            context = {
                
                "form": form
            }
            messages.warning(request, f"Booking failed!")
            return render(request, "book.html", context)

    def get(self, request):
        form = BookingForm()
        context = {
            "form": form,
            "active": "book"
        }
        return render(request, "book.html", context)


class BookingSearch(View):
    def post(self, request):
        if request.POST.get("action") == "viewbook":
            booking_no = request.POST.get('booking-number', '')
            return redirect(reverse("edit_booking", args=([booking_no])))

    def get(self, request):
        form = BookingForm()
        context = {
            "form": form,
        }
        return render(request, "open-booking.html", context)


class BookingEdit(View):
    def post(self, request, booking_no):
        if Booking.objects.filter(booking_no=booking_no).exists():
            bookingitem = get_object_or_404(Booking, booking_no=booking_no)
            form = BookingForm(request.POST, instance=bookingitem)
            filledform = BookingForm(instance=bookingitem)
            context = {
                    "form": filledform,
                }
            print(request.POST)
            if request.POST.get("Action") == "Delete":
                return redirect(reverse("delete_booking", args=([booking_no])))

            if form.is_valid():
                form.save()
                messages.success(request, "Update successfull!")
                return render(request, "edit-booking.html", context)

            if not form.is_valid():
                messages.error(request, "Update was not successfull!")
                return render(request, "edit-booking.html", context)

        elif not Booking.objects.filter(booking_no=booking_no).exists():
            messages.error(request, "Booking was not found!")
            return redirect(reverse("open_booking", args=([booking_no])))

    def get(self, request, booking_no):
        if Booking.objects.filter(booking_no=booking_no).exists():
            bookingitem = get_object_or_404(Booking, booking_no=booking_no)
            filledform = BookingForm(instance=bookingitem)
            context = {
                "form": filledform,
            }
            print(filledform)
            return render(request, "edit-booking.html", context)

        elif not Booking.objects.filter(booking_no=booking_no).exists():
            messages.error(request, "Booking was not found!")
            return redirect(reverse("open_booking", args=([booking_no])))


class DeleteBooking(View):
    def get(self, request, booking_no):
        bookingitem = get_object_or_404(Booking, booking_no=booking_no)
        bookingitem.delete()
        messages.success(request, "Booking deleted!")
        return redirect(reverse("open_booking"))


class ShowAllBookings(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = "/accounts/login/"
    permission_required = ("booking.view_booking", "booking.add_booking", "booking.delete_booking", "booking.change_booking")
    model = Booking
    queryset = Booking.objects.all().order_by("-date", "-time")
    template_name = "view-booking.html"
    paginate_by = 10


class CheckBookings(View):
    def get(self, request):        
        booking_date = request.GET.get("date")
        booking_time = request.GET.get("time")
        booking_tablesize = request.GET.get("tablesize")
        print(request.GET)
        if booking_date == "":
            return JsonResponse({"tableAvailable": True})
        elif len(Booking.objects.filter(
                                        time=booking_time,
                                        date=booking_date,
                                        tablesize=booking_tablesize)
                 ) > 3:
            return JsonResponse({"tableAvailable": False})
        else:
            return JsonResponse({"tableAvailable": True})
