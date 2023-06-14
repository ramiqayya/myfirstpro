from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, "exams/home.html")


def takeha(request, andy):
    return HttpResponse(f"takfeen ya {andy.capitalize()}")
