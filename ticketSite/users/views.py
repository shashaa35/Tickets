from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
# from .forms import UserRegistrationForm, UserUpdateForm, UserProfileUpdateForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        return redirect('ticketsHome')
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            locationType = form.cleaned_data.get('locationType')
            user = CustomUser.objects.get(phone=phone)
            user.save()
            return redirect('login')
        else:
            context = {'form': form}
            return render(request, 'users/register.html', context)
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

def editProfile(request):
    user = request.user

    if request.method == 'POST':
        p_form = CustomUserChangeForm(request.POST, instance=user)
        if p_form.is_valid():
            p_form.save()
            return redirect('ticketsHome')
    else:
        p_form = CustomUserChangeForm(instance=user)
    context = {'p_form': p_form}
    return render(request, 'users/editProfile.html', context)
