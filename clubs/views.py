from django.shortcuts import render
from django.urls import reverse
from .models import ClubProfile
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ClubDetailForm


def clubs_list(request):
    template = loader.get_template('clubs/clubs.html')
    club = ClubProfile.objects.all()
    context = {
        'club':club
    }
    return HttpResponse(template.render(context, request))


def club_create_view(request):
    template = loader.get_template('clubs/create_club.html')
    context = {}
    form = ClubDetailForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('clubs:club-list'))
    context['form'] = form
    return HttpResponse(template.render(context, request))