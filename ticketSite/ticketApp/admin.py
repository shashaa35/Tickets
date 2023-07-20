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
    can_delete = False
    verbose_name_plural = 'userprofile'
    fk_name = 'user'

class UserProfileAdmin(UserAdmin):
    inlines = [ UserProfileInline, ]
    list_display = ('username', 'email', 'get_name', 'is_staff', 'get_locationType')

    def get_locationType(self, instance):
        return instance.userprofile.locationType
    get_locationType.short_description = 'Location Type'
    
    def get_name(self, instance):
        return instance.userprofile.name
    get_name.short_description = 'Name'
    
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserProfileAdmin, self).get_inline_instances(request, obj)

admin.site.register(User, UserProfileAdmin)
