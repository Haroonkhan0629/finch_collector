from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ("B", "Breakfast"),
    ("L", "Lunch"),
    ("D", "Dinner"),
)

# Create your models here.

class Bird(models.Model):
    name = models.CharField(max_length=100)
    image = models.TextField(max_length=250)
    scientific_name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    wingspan = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={'bird_id': self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
    
class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        choices = MEALS,
        default = MEALS[0][0]
        )
    
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']