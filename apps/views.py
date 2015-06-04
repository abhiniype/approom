from django.shortcuts import render
from django.views.generic.list import ListView
from apps.models import App

class AppList(ListView):
    model = App
