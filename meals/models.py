from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class MealImage(models.Model):
    meal = models.ForeignKey(Meal, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='meal_images/')  # Handles both images and videos

    def __str__(self):
        return f"{self.meal.name} Image"
