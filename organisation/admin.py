from django.contrib import admin
from .models import OrgProfile

@admin.register(OrgProfile)
class OrgProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'org_name')
