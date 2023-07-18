from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ticketList", views.ticketList, name="ticketList"),
    path("ticket/<int:ticket_id>", views.ticket, name="ticket"),
    path("createTicket", views.createTicket, name="createTicket"),
    path("editTicketForStaff/<int:ticket_id>", views.editTicketForStaff, name="editTicketForStaff"),
]