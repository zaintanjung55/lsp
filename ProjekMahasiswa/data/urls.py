from django.contrib import admin
from django.urls import path
from . import views

app_name = 'data'

urlpatterns = [
    path('', views.hello, name='hello'),
    path('form/', views.form, name='form'),
    
]
