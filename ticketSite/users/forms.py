from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import LOCATION_TYPE_CHOICES, UserProfile

class UserRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=101)
    designation = forms.CharField(max_length=101)
    phone_regex = RegexValidator(regex=r'^[0-9]{10}$', message="Phone number must be entered without +91, or 0.")
    phone = forms.CharField(validators=[phone_regex], max_length=10)
    address = forms.CharField(max_length=101)
    locationType = forms.ChoiceField(choices=LOCATION_TYPE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'name', 'designation', 'phone', 'locationType', 'address', 'email', 'password1', 'password2']