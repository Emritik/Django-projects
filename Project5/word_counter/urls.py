from django.urls import path
from . import views

urlpatterns = [
    path('',views.counter, name="counter"),
]
