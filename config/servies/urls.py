from django.urls import path, include
from .views import servies

urlpatterns = [
    path('', servies),
]