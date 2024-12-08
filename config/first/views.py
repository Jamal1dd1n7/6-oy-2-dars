from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

def home(request: WSGIRequest):
    return render(request, 'first.html')
