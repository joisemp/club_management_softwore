from django.shortcuts import render
from django.views import generic
from .mixins import OrgOnlyAccessMixin


class OrgProfilePageView(OrgOnlyAccessMixin, generic.TemplateView):
    template_name = 'org/profile.html'
    

class OrgDashboardView(OrgOnlyAccessMixin, generic.TemplateView):
    template_name = 'org/dashboard.html'
