from django.urls import path
from . import views

urlpatterns = [
    path('tickets/', views.tickets, name="tickets")
]