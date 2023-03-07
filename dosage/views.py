from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sandanam(request):
    return HttpResponse('<marquee><h1>Drugs are Ready to import</h1></marquee>')