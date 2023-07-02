from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import QuestionForm, ChoiceForm
from django import forms
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
from .models import User, Question, Choice
from django.db import IntegrityError


@login_required(login_url='/login')
def index(request):
    return render(request, "exams/home.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "exams/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "exams/login.html")


def profile(request):

    question = Question.objects.order_by('?')[0]
    choices = Choice.objects.filter(question=question)
    print(choices.filter(is_correct=True))
    if request.method == "POST":

        try:
            zafaste = request.POST["takeha"]
            print(zafaste)

            question = Question.objects.order_by('?')[0]
            choices = Choice.objects.filter(question=question)
        except MultiValueDictKeyError:
            return render(request, "exams/profile.html", {
                "error": "Boht Moskel choose something",



            })

        return render(request, "exams/profile.html", {
            "message": "Ich bin du",
            "question": question,
            "choices": choices


        })

    # questions = {"question1": "why like this?",
    #              "choice 1": {
    #                  "answer": "ich bin du",
    #                  "isCorrect": True
    #              },
    #              "choice 2": {
    #                  "answer": "Takeha",
    #                  "isCorrect": False
    #              },
    #              "choice 3": {
    #                  "answer": "Sawade ka",
    #                  "isCorrect": False
    #              },
    #              "choice 4": {
    #                  "answer": "Danti",
    #                  "isCorrect": False
    #              },

    #              }

    return render(request, "exams/profile.html", {
        "message": "Ich bin du",
        "question": question,
        "choices": choices


    })


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "exams/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "exams/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "exams/register.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def takeha(request, andy):
    return HttpResponse(f"takfeen ya {andy.capitalize()}")
