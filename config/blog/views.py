from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

def blog(request: WSGIRequest):
    return render(request, 'blog.html')

def about(request: WSGIRequest):
    return render(request, 'about.html')
