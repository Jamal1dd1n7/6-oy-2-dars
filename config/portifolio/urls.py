from django.urls import path, include
from .views import portifolio

urlpatterns = [
    path('', portifolio),
]