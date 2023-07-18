from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from users.models import UserProfile

# Register your models here.
from .models import Ticket, ProblemType, ProblemSubtype

admin.site.unregister(User)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'description', 'created_by','updated_at')
    search_fields = ['status']

@admin.register(ProblemType)
class ProblemTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'created_at', 'updated_at')

@admin.register(ProblemSubtype)
class ProblemSubtypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'problem_type', 'created_at', 'updated_at')

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserProfileAdmin(UserAdmin):
    inlines = [ UserProfileInline, ]
admin.site.register(User, UserProfileAdmin)
