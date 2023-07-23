from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)

def home(request):
    logger.info('Home page accessed')
    if request.user.is_authenticated:
        logger.info('User is authenticated and redirected to tickets home page')
        return redirect('ticketsHome')
    else:
        logger.info('User is not authenticated and redirected to login page')
    return redirect('login')

def register(request):
    logger.info('Register page accessed')
    if request.method == 'POST':
        logger.info('POST request received')
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            logger.info('Form is valid')
            form.save()
            logger.info('User created')
            return redirect('login')
        else:
            context = {'form': form}
            logger.info('Form is invalid with errors: ' + str(form.errors))
            logger.info('Context is: ' + str(context))
            return render(request, 'users/register.html', context)
    else:
        logger.info('GET request received')
        form = CustomUserCreationForm()

    context = {'form': form}
    logger.info('Context is: ' + str(context))
    return render(request, 'users/register.html', context)

@login_required(login_url='login')
def editProfile(request):
    logger.info('Edit profile page accessed by user: ' + str(request.user))
    user = request.user
    if request.method == 'POST':
        logger.info('POST request')
        p_form = CustomUserChangeForm(request.POST, instance=user)
        if p_form.is_valid():
            logger.info('Form is valid')
            p_form.save()
            logger.info('User profile updated')
            return redirect('ticketsHome')
    else:
        logger.info('GET request')
        p_form = CustomUserChangeForm(instance=user)
    context = {'p_form': p_form}
    logger.info('Context is: ' + str(context))
    return render(request, 'users/editProfile.html', context)
