from django import forms
from .models import Booking
from phonenumber_field.formfields import PhoneNumberField


class DateInput(forms.DateInput):
    input_type = "date"


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = (
            "firstname",
            "lastname",
            "email",
            "phonenumber",
            "date",
            "time",
            "tablesize",
        )
        widgets = {
            "date": DateInput(),
        }
