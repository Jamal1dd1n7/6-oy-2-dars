from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

def contact(request: WSGIRequest):
    return render(request, 'contact.html')
