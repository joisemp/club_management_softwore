from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic
from .mixins import OrgOnlyAccessMixin
from accounts.models import StudentProfile
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from accounts.forms import StudentProfileForm


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


def student_edit_view(request, id):
    template = loader.get_template('org/edit_student.html')
    context = {}
    student_profile = StudentProfile.objects.get(id=id)
    form = StudentProfileForm(request.POST or None, instance=student_profile)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('org:student-list'))
    context['form'] = form
    if request.user.is_authenticated and request.user.is_org:
        return HttpResponse(template.render(context, request))
    else:
        return redirect('org:student-list')
    
    
def student_delete_view(request, id):
    template = loader.get_template('org/delete_student.html')
    context = {}
    student_profile = StudentProfile.objects.get(id=id)
    context['student_profile'] = student_profile
    if request.method == 'POST':
        user = student_profile.user
        user.delete()
        student_profile.delete()
        return HttpResponseRedirect(reverse('org:student-list'))
    if request.user.is_authenticated and request.user.is_org:
        return HttpResponse(template.render(context, request))
    else:
        return redirect('landing-page')
