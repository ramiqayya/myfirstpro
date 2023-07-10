from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
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
    if request.method == 'POST':
        question_choices = {}
        for question in Question.objects.all():
            choice_id = request.POST.get('question_{}'.format(question.id))
            if choice_id:
                question_choices['question_{}'.format(
                    question.id)] = int(choice_id)
        request.session['question_choices'] = question_choices

    questions = Question.objects.all()
    paginator = Paginator(questions, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "exams/profile.html", {
        "message": "Ich bin du",
        "question": questions,
        "page_obj": page_obj
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
