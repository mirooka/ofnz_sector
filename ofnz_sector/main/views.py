from django.views import generic as views
from django.shortcuts import render


# Create your views here.

class HomeView(views.TemplateView):
    template_name = 'main/home_page.html'

