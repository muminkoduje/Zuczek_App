from django.contrib import admin
from django.urls import path
from .views import main,home1
urlpatterns = [
    path('',main),
    path('Home',home1)
]

