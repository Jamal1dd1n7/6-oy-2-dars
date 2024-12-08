from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

def servies(request: WSGIRequest):
    return render(request, 'servies.html')
