from django import forms
from .models import Meal, MealImage

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'ingredients', 'description']


class MealImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = MealImage
        fields = ['image']
