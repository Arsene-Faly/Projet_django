from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def acceuil_views(request):
    return HttpResponse("Bienvenue sur Django")

def apropos_views(request):
    return HttpResponse("Page d'aprpos")

def service_views(request):
    return HttpResponse("Page de service")

def contact_views(request):
    return HttpResponse("Page de contact")