from django.shortcuts import render
from django.http import HttpResponse


def clubs_list(request):
    return HttpResponse("club home")
