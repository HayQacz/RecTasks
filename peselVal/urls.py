from django.urls import path
from . import views

urlpatterns = [
    path('', views.validate_pesel_view, name='validate_pesel'),
]