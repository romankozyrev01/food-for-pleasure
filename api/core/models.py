from django.db import models
from users.models import CustomUser


class Meal(models.Model):
    name = models.CharField(max_length=255)
    calories = models.IntegerField()
    proteins = models.IntegerField()
    fats = models.IntegerField()
    carbohydrates = models.IntegerField()
    weight = models.IntegerField

    def __str__(self):
        return f"{self.name}"


class Activity(models.Model):
    name = models.CharField(max_length=255)
    duration = models.TimeField()
    burned_calories = models.IntegerField()


class ActivityUser(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)


class MealUser(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
