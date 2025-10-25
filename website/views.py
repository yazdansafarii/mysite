from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_view(request):
    return HttpResponse('home page')

def about_view(request):
    return HttpResponse('aboute')


def contact_view(request):
    return HttpResponse('contacte')