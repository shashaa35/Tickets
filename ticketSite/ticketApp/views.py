from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import TicketForm, TicketUpdateForm
from .models import Ticket
from users.models import CustomUser
import logging

logger = logging.getLogger(__name__)

# tickets home page
@login_required(login_url='login/')
def index(request):
    logger.info('Tickets home page accessed by user: ' + str(request.user))
    return render(request, 'tickets/index.html')

# get all tickets created by the user
@login_required(login_url='login')
def ticketList(request):
    logger.info('Tickets list page accessed by user: ' + str(request.user))
    if request.user.is_superuser:
        logger.info('User is superuser')
        ticketsCreatedByUser = Ticket.objects.all()
        user_profiles = CustomUser.objects.all()
    elif request.user.groups.filter(name = 'Staff').exists():
        logger.info('User is staff')
        location_of_staff = CustomUser.objects.get(id=request.user.id).locationType
        ticketsCreatedByUser = Ticket.objects.filter(created_by__locationType=location_of_staff)
        user_profiles = CustomUser.objects.filter(locationType=location_of_staff)
    else:
        logger.info('User is not staff')
        ticketsCreatedByUser = Ticket.objects.filter(created_by=request.user)
        user_profiles = CustomUser.objects.filter(id=request.user.id)
    
    logger.info('Tickets are: ' + str(ticketsCreatedByUser))
    logger.info('User profiles are: ' + str(user_profiles))
    for ticket in ticketsCreatedByUser:
        ticket.user_profile = user_profiles.get(id=ticket.created_by.id)
    context = {
        'ticketsCreatedByUser': ticketsCreatedByUser
    }
    logger.info('Context is: ' + str(context))
    return render(request, 'tickets/ticketList.html', context)

# get particular ticket by id
@login_required(login_url='login')
def ticket(request, ticket_id):
    logger.info('Ticket page accessed by user: ' + str(request.user))
    if request.user.groups.filter(name = 'Staff').exists():
        logger.info('User is staff')
        ticket_details = Ticket.objects.get(id=ticket_id)
        user_profiles = CustomUser.objects.all()
    else:
        logger.info('User is not staff')
        ticket_details = Ticket.objects.get(id=ticket_id, created_by=request.user)
        user_profiles = CustomUser.objects.filter(id=request.user.id)
    ticket_details.user_profile = user_profiles.get(id=ticket_details.created_by.id)
    context = {
        'ticket_details': ticket_details
    }
    logger.info('Context is: ' + str(context))
    return render(request, 'tickets/ticket.html', context)

# create a new ticket
@login_required(login_url='login')
def createTicket(request):
    logger.info('Create ticket page accessed by user: ' + str(request.user))
    if request.method == 'POST':
        logger.info('POST request')
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            logger.info('Form is valid')
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            logger.info('Ticket created')
            return redirect('/tickets')
        else:
            context = {
                'form': form
            }
            logger.info('Form is invalid with errors: ' + str(form.errors))
            logger.info('Context is: ' + str(context))
            return render(request, 'tickets/createTicket.html', context)
    else:
        form = TicketForm()
        context = {
            'form': form
        }
        logger.info('Context is: ' + str(context))
    return render(request, 'tickets/createTicket.html', context)

# edit a ticket
@login_required(login_url='login')
def editTicketForStaff(request, ticket_id):
    logger.info('Edit ticket page accessed by user: ' + str(request.user))
    if request.user.groups.filter(name = 'Staff').exists():
        logger.info('User is staff')
        ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        logger.info('POST request')
        form = TicketUpdateForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            logger.info('Form is valid')
            form.save()
            logger.info('Ticket updated')
            return redirect('/tickets')
        else:
            context = {
                'form': form
            }
            logger.info('Form is invalid with errors: ' + str(form.errors))
            logger.info('Context is: ' + str(context))
            return render(request, 'tickets/editTicket.html', context)
    else:
        logger.info('GET request for edit ticket')
        form = TicketUpdateForm(instance=ticket)
        context = {
            'form': form
        }
        logger.info('Context is: ' + str(context))
    return render(request, 'tickets/editTicket.html', context)