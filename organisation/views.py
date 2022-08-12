from django.shortcuts import render
from django.views import generic
from . models import StaffProfile


class OrgDashboardView(generic.TemplateView):
    template_name = 'organisation/org_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(OrgDashboardView, self).get_context_data(**kwargs)
        context['staffs'] = StaffProfile.objects.filter(
            org=self.request.user.orgprofile)
        return context
