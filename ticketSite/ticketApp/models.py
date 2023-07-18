from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
class TicketStatus(models.TextChoices):
    CREATED = 'Created' # When a ticket is created, it is in this state, and waiting for a RW Officer to approve it.
    APPROVED_BY_RW_OFFICER = 'Approved by RW Officer' # When a ticket is approved by a RW Officer, Contractor can start working on it.
    TO_DO = 'To Do' # Ticket is yet to start being worked on.
    IN_PROGRESS = 'In Progress' # Ticket is being worked on.
    IN_REVIEW = 'In Review' # Ticket is being reviewed by a RW Officer/Contractor.
    DONE = 'Done' # Ticket is done.

class ProblemType(models.Model):
    type = models.CharField(max_length=1000)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)
    created_by = models.ForeignKey(User, null=True, blank = True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.type

class ProblemSubtype(models.Model):
    type = models.CharField(max_length=1000)
    problem_type = models.ForeignKey(ProblemType, null=True, blank = True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)
    created_by = models.ForeignKey(User, null=True, blank = True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.type

class Ticket(models.Model):
    title = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    problemType = models.ForeignKey(ProblemType, null=True, blank = True, on_delete=models.SET_NULL)
    problemSubtype = ChainedForeignKey(
        ProblemSubtype,
        chained_field="problemType",
        chained_model_field="problem_type",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True,
        blank = True,
        on_delete=models.SET_NULL)
    description = models.TextField()
    created_by = models.ForeignKey(User, null=True, blank = True, on_delete=models.SET_NULL, related_name='created_by')
    status = models.CharField(max_length=1000, choices=TicketStatus.choices, default=TicketStatus.CREATED)
    assignee = models.ForeignKey(User, null=True, blank = True, on_delete=models.SET_NULL, related_name='assignee')
    hours_spent = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)

    def __str__(self):
        return self.title