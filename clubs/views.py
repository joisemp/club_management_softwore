from django.shortcuts import redirect, render
from django.urls import reverse
from .models import ClubProfile
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ClubCreateForm, ClubEditForm


def clubs_list(request):
    template = loader.get_template('clubs/clubs.html')
    context = {}
    context['clubs'] = ClubProfile.objects.all()
    return HttpResponse(template.render(context, request))


def club_create_view(request):
    template = loader.get_template('clubs/create_club.html')
    context = {}
    form = ClubCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('clubs:club-list'))
    context['form'] = form
    if request.user.is_authenticated and request.user.is_org:
        return HttpResponse(template.render(context, request))
    else:
        return redirect('clubs:club-list')


def club_detail_view(request, id):
    template = loader.get_template('clubs/club_details.html')
    context = {}
    context['club'] = ClubProfile.objects.get(id=id)
    return HttpResponse(template.render(context, request))


def club_edit_view(request, id):
    template = loader.get_template('clubs/edit_club.html')
    context = {}
    club = ClubProfile.objects.get(id=id)
    form = ClubEditForm(request.POST or None, instance=club)
    if form.is_valid():
        instance = form.save()
        return HttpResponseRedirect(reverse('clubs:club-detail', args=[instance.pk]))
    context['form'] = form
    if request.user.is_authenticated and request.user.is_org:
        return HttpResponse(template.render(context, request))
    else:
        return redirect('clubs:club-list')


def club_delete_view(request, id):
    template = loader.get_template('clubs/delete_club.html')
    context = {}
    club = ClubProfile.objects.get(id=id)
    context['club'] = club
    if request.method == 'POST':
        club.delete()
        return HttpResponseRedirect(reverse('clubs:club-list'))
    if request.user.is_authenticated and request.user.is_org:
        return HttpResponse(template.render(context, request))
    else:
        return redirect('clubs:club-list')
