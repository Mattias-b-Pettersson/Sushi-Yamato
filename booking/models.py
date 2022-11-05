from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid

TABLESIZE_CHOISES = (
    ("2", "2"),
    ("4", "4"),
    ("6", "6"),
    ("8", "8"),
)
TIME_CHOISES = (
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
    ("18:00", "18:00"),
    ("19:00", "19:00"),
    ("20:00", "20:00"),
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
    time = models.CharField(max_length=20, choices=TIME_CHOISES,
                                 default="10")
    tablesize = models.CharField(max_length=20, choices=TABLESIZE_CHOISES,
                                 default="2")

    def __str__(self):
        return self.booking_no
