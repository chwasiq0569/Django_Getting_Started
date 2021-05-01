from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner")


def date(request):
    return HttpResponse("This Page was served at " + str(datetime.now()))
# Create your views here.
