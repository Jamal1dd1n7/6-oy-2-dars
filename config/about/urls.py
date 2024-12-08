from django.urls import path, include
from .views import about, blog

urlpatterns = [
    path('', about),
    path('blog/', blog),
    path('servies/', include('servies.urls')),
    path('portifolio/', include('portifolio.urls')),
    path('contact/', include('contact.urls')),
]