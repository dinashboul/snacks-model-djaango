from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Snacks
# Create your views here.
class HomePage(TemplateView):
    template_name = 'home.html'
    
class SnackListView(ListView):
    template_name='snacks.html'
    model=Snacks 
