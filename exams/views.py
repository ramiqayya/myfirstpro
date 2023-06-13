from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<button>Hello world</button>")


def takeha(request, andy):
    return HttpResponse(f"takfeen ya {andy.capitalize()}")
