from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'cv/base.html')

def blogsingle(request):
    return render(request, 'blog-single.html')