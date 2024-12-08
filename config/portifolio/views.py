from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

def portifolio(request: WSGIRequest):
    return render(request, 'portifolio.html')
