from django.shortcuts import render
from .models import ClubProfile
from django.template import loader
from django.http import HttpResponse


def clubs_list(request):
    template = loader.get_template('clubs/clubs.html')
    club = ClubProfile.objects.all()
    context = {
        'club':club
    }
    return HttpResponse(template.render(context, request))
