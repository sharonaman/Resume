from django.urls import path
from . import views
from django.urls import path, include
from .views import base
from .views import submit_form



urlpatterns = [
    path('index/', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('blogsingle/', views.blogsingle, name='blogsingle'),
    path('submit/', submit_form, name='submit_form'),
    path('', submit_form, name='submit_form'),

]


