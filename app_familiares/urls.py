from django.contrib import admin
from django.urls import path
from app_familiares.views import yo, familiares

urlpatterns = [
    path('yo/', yo),
    path('familiares/', familiares),
]