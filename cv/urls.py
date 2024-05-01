from django.urls import path
from . import views
from django.urls import path, include
from .views import base


urlpatterns = [
    path('index/', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('blogsingle/', views.blogsingle, name='blogsingle'),

]


