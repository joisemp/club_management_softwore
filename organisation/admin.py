from django.contrib import admin
from .models import OrgProfile, StaffProfile


@admin.register(OrgProfile)
class OrgProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'org_name')


@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ('org', 'first_name', 'last_name', 'email')
