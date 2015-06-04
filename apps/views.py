from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from apps.models import App

class AppList(ListView):
    model = App
    
class AppDetail(DetailView):
    model = App
