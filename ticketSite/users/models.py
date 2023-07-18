from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this
# Create your models here.

LOCATION_TYPE_CHOICES = (
    ('Quarter', 'Quarter'),
    ('Building', 'Building'),
    ('Other', 'Other'),
)

from django.core.validators import RegexValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=101)
    designation = models.CharField(max_length=101)
    phone_regex = RegexValidator(regex=r'^[0-9]{10}$', message="Phone number must be entered without +91, or 0.")
    phone = models.CharField(validators=[phone_regex], max_length=10)
    address = models.CharField(max_length=101)
    locationType = models.CharField(max_length=101)