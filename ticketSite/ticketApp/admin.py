from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Ticket, ProblemType, ProblemSubtype
from django.contrib.auth.models import Group 

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_locationType', 'description', 'created_by', 'problemType', 'problemSubtype', 'updated_at')
    search_fields = ['status']

    def get_locationType(self, instance):
        return instance.created_by.locationType
    
    get_locationType.short_description = 'Location'

@admin.register(ProblemType)
class ProblemTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'created_at', 'updated_at')

@admin.register(ProblemSubtype)
class ProblemSubtypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'problem_type', 'created_at', 'updated_at')

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("name", "locationType", "phone", "get_is_staffMember")
    list_filter = ("phone", "name", "locationType",)

    def get_is_staffMember(self, instance):
        return Group.objects.get(name='Staff') in instance.groups.all()
    
    get_is_staffMember.short_description = 'Staff Member'

    fieldsets = (
        (None, {"fields": ("phone", "password", "name", "address", "locationType")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "phone", "name", "address","locationType", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("phone",)
    ordering = ("name",)

admin.site.register(CustomUser, CustomUserAdmin)