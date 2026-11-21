from django.urls import path
from .views import acceuil_views, apropos_views, service_views, contact_views

urlpatterns = [
    path('', acceuil_views, name="home"),
    path('apropos/', apropos_views, name="about"),
    path('service/', service_views, name="service"),
    path('contact/', contact_views, name="contact"),
]
