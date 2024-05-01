from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MyForm


def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'cv/base.html')

def blogsingle(request):
    return render(request, 'blog-single.html')


def submit_form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data to the database
            return redirect('success')  # Redirect to a success page
    else:
        form = MyForm()
    return render(request, 'index.html', {'form': form})

