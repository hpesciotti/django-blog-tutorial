from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import About


# Create your views here.
class AboutList(generic.ListView):
    queryset = About.objects.first()
    template_name = "about/about.html"
