from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import TicketForm, TicketUpdateForm
from .models import Ticket, ProblemType, TicketStatus, ProblemSubtype
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

# tickets home page
@login_required(login_url='login/')
def index(request):
    # return "hello"
    return render(request, 'tickets/index.html')

# get all tickets created by the user
@login_required(login_url='login')
def ticketList(request):
    if request.user.groups.filter(name = 'Staff').exists():
        ticketsCreatedByUser = Ticket.objects.all()
    else:
        ticketsCreatedByUser = Ticket.objects.filter(created_by=request.user)
    user = request.user
    context = {
        'ticketsCreatedByUser': ticketsCreatedByUser,
        'user': user
    }
    return render(request, 'tickets/ticketList.html', context)

# get particular ticket by id
@login_required(login_url='login')
def ticket(request, ticket_id):
    if request.user.groups.filter(name = 'Staff').exists():
        ticket_details = Ticket.objects.get(id=ticket_id)
    else:
        ticket_details = Ticket.objects.get(id=ticket_id, created_by=request.user)
    user_details = User.objects.get(id=ticket_details.created_by.id)
    context = {
        'ticket_details': ticket_details,
        'user_details': user_details
    }
    print(ticket_details)
    print(user_details.userprofile.locationType)
    return render(request, 'tickets/ticket.html', context)

# create a new ticket
@login_required(login_url='login')
def createTicket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            return redirect('tickets/ticketList')
        else:
            context = {
                'form': form
            }
            return render(request, 'tickets/createTicket.html', context)
    else:
        form = TicketForm()
        context = {
            'form': form
        }
    return render(request, 'tickets/createTicket.html', context)

# edit a ticket
@login_required(login_url='login')
def editTicketForStaff(request, ticket_id):
    if request.user.groups.filter(name = 'Staff').exists():
        ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        form = TicketUpdateForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('tickets/ticketList')
        else:
            context = {
                'form': form
            }
            return render(request, 'tickets/editTicket.html', context)
    else:
        form = TicketUpdateForm(instance=ticket)
        context = {
            'form': form
        }
    return render(request, 'tickets/editTicket.html', context)