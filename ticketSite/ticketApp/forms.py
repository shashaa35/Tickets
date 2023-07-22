from django import forms

from .models import Ticket, ProblemType, ProblemSubtype

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ("created_by", "status", "updated_at", "assignee", "hours_spent", "title")


class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ("created_by", "updated_at", "title")