from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    # return HttpResponse("hello world!")
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'
