from django.db import models

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
    phonenumber = models.IntegerField()
    email = models.EmailField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    tablesize = models.CharField(max_length=20, choices=TABLESIZE_CHOISES,
                                 default='2')

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
