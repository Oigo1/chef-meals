from django.shortcuts import render, redirect
from .forms import MealForm, MealImageForm
from .models import Meal, MealImage

def create_meal(request):
    if request.method == 'POST':
        meal_form = MealForm(request.POST)
        images_form = MealImageForm(request.POST, request.FILES)
        
        if meal_form.is_valid():
            meal = meal_form.save()
            images = request.FILES.getlist('image')
            for img in images:
                MealImage.objects.create(meal=meal, image=img)
            return redirect('meal_list')
    
    else:
        meal_form = MealForm()
        images_form = MealImageForm()

    meals = Meal.objects.all()
    return render(request, 'meals/create_meal.html', {
        'meal_form': meal_form,
        'images_form': images_form,
        'meals': meals
    })
