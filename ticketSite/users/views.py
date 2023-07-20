from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import UserProfile
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        return redirect('ticketsHome')
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            designation = form.cleaned_data.get('designation')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            locationType = form.cleaned_data.get('locationType')
            user = User.objects.get(username=form.cleaned_data.get('username'))
            user_profile = UserProfile(user=user, name=name, designation=designation, phone=phone, address=address, locationType=locationType)
            user_profile.save()
            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)