from django.shortcuts import render
from django.views import generic
from .mixins import OrgOnlyAndLoginRequiredMixin


class OrgProfilePageView(OrgOnlyAndLoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/profile.html'
