from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import Post

# Create your views here.

# Deleted
# def index(request):
#     return HttpResponse("Hello, Blog")


class PostList(generic.ListView):
    model = Post