from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Kitchen(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    appliance = models.CharField(max_length=50)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    hour_use_day = models.IntegerField(validators=[MaxValueValidator(24)])
    times_week = models.IntegerField(validators=[MaxValueValidator(7)])

    def __str__(self):
        # return what do you want to show on the screen if we just access one of these recods.
        return(f'({self.appliance} {self.brand} {self.model})')