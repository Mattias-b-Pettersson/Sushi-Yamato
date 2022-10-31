from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid

TABLESIZE_CHOISES = (
    ("2", "2"),
    ("4", "4"),
    ("6", "6"),
    ("8", "8"),
)


def unique_uuid():
    # Generate ID once, then check the db. If id exists, keep trying.
    temp_booking_no = uuid.uuid4().hex[:10]
    while Booking.objects.filter(booking_no=temp_booking_no).exists():
        temp_booking_no = uuid.uuid4().hex[:10]
    return temp_booking_no


class Booking(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    booking_no = models.CharField(unique=True, default=unique_uuid, max_length=10, editable=False)
    phonenumber = PhoneNumberField(blank=True)
    email = models.EmailField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    tablesize = models.CharField(max_length=20, choices=TABLESIZE_CHOISES,
                                 default='2')

    def __str__(self):
        return f"{self.firstname} {self.lastname}, {self.booking_no}"
