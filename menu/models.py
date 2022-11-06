from django.db import models
from django.utils.text import slugify

# Create your models here.

FOOD_TYPES = (
        ('rolls', 'rolls'),
        ('sushi', 'sushi'),
        ('warm', 'warm'),
        ('bowls', 'bowls'),
)

DRINK_TYPES = (
        ('warm', 'warm'),
        ('cold', 'cold'),
        ('beer', 'beer'),
        ('wine', 'wine'),
        ('sake', 'sake'),
)


class FoodItem(models.Model):
        name = models.CharField(max_length=100, unique=True)
        slug = models.SlugField(blank=True, null=True)
        description = models.CharField(max_length=300)
        price = models.CharField(max_length=50)
        type = models.CharField(max_length=100, choices=FOOD_TYPES)
        
        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super().save(*args, **kwargs)


class DrinkItem(models.Model):
        name = models.CharField(max_length=100, unique=True)
        slug = models.SlugField(blank=True, null=True)
        description = models.CharField(max_length=300)
        price = models.CharField(max_length=50)
        type = models.CharField(max_length=100, choices=DRINK_TYPES)

        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super().save(*args, **kwargs)
        