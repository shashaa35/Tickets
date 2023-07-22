from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
# Create your models here.

LOCATION_TYPE_CHOICES = (
    ('North Colony', 'North Colony'),
    ('South Colony', 'South Colony'),
    ('Service Building', 'Service Building'),
    ('Agra', 'Agra'),
    ('Other', 'Other'),
)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator(regex=r'^[0-9]{10}$', message="Phone number must be entered without +91, or 0.")
    phone = models.CharField(unique=True, validators=[phone_regex], max_length=10)
    address = models.CharField(max_length=101)
    locationType = models.CharField(max_length=101, choices=LOCATION_TYPE_CHOICES)
    name = models.CharField(max_length=101)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["address", "locationType", "name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.name