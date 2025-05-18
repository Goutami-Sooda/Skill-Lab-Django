from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django! Welcome to the To-Do App.")
