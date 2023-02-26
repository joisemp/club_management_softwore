from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.forms import CheckboxSelectMultiple

from .models import User, StudentProfile


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    fieldsets = (
        (_('User'), {'fields': ('first_name', 'last_name', 'email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','is_org', 'is_student', 'groups')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    readonly_fields = ('date_joined', 'last_login')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'is_active','is_org','is_student', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ()
    

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('org', 'first_name', 'last_name', 'email')