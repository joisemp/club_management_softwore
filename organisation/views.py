from django.shortcuts import render
from django.views import generic


class OrgDashboardView(generic.TemplateView):
    template_name = 'organisation/org_dashboard.html'
