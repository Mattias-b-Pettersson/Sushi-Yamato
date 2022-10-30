from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

TABLESIZE_CHOISES = (
    ("2", "2"),
    ("4", "4"),
    ("6", "6"),
    ("8", "8"),
)


class Booking(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    phonenumber = PhoneNumberField(blank=True)
    email = models.EmailField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    tablesize = models.CharField(max_length=20, choices=TABLESIZE_CHOISES,
                                 default='2')

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
