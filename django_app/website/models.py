from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save #serch about it!!
from django.dispatch import receiver #serch about it!!

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)

#Create a signal to automatically create a UserProfile instance when a new User is created:
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

#records timeline 
class Kitchen(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    appliance = models.CharField(max_length=50)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    hour_use_day = models.IntegerField(validators=[MaxValueValidator(24)])
    times_week = models.IntegerField(validators=[MaxValueValidator(7)])
    power_rate = models.IntegerField()
    consumption_rate = models.CharField(max_length=50)

    # __str__ Method in the model is primarily used for debugging purposes and to provide a string representation when an instance is displayed in the Django admin or other contexts.
    def __str__(self):
        # return what do you want to show on the screen if we just access one of these recods.
        return(f'({self.appliance} {self.brand})')