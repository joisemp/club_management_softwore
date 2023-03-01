from django.shortcuts import render
from django.views import generic
from .mixins import OrgOnlyAccessMixin
from accounts.models import StudentProfile


class OrgProfilePageView(OrgOnlyAccessMixin, generic.TemplateView):
    template_name = 'org/profile.html'
    

class OrgDashboardView(OrgOnlyAccessMixin, generic.TemplateView):
    template_name = 'org/dashboard.html'
    

class StudentListView(OrgOnlyAccessMixin, generic.ListView):
    template_name = 'org/student_list.html'
    model = StudentProfile
    context_object_name = 'students'
    
    def get_queryset(self, **kwargs):
       student_profile = super().get_queryset(**kwargs)
       return student_profile.filter(org=self.request.user.orgprofile).order_by('-id')
