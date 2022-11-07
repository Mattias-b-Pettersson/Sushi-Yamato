from django import forms
from .models import FoodItem, DrinkItem



class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem()
        fields = ("name", "description", "price", "type")


class DrinkItemForm(forms.ModelForm):
    class Meta:
        model = DrinkItem()
        fields = ("name", "description", "price", "type")