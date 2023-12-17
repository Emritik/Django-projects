from django.contrib import admin
from django.urls import path 
from Todo_App import views

urlpatterns = [
    path("",views.index,name='Home'),
    path("delete/<id>/",views.delete, name='Delete'),
    path("edit/<id>/",views.edit, name='Edit')
]
