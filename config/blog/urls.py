from django.urls import path, include
from .views import blog, about

urlpatterns = [
    path('', blog),
    path('/about/', about),
]