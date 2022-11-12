from django.db import models
from django.utils.text import slugify

# Create your models here.

MENU_TYPES = (
        ('rolls', 'rolls'),
        ('sushi', 'sushi'),
        ('warm food', 'warm food'),
        ('bowls', 'bowls'),
        ('warm beverage', 'warm beverage'),
        ('cold beverage', 'cold beverage'),
        ('beer', 'beer'),
        ('wine', 'wine'),
        ('sake', 'sake'),
)


class MenuItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True, null=True)
    description = models.CharField(max_length=300)
    price = models.CharField(max_length=50)
    type = models.CharField(max_length=100, choices=MENU_TYPES)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
