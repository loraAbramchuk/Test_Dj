from django.template.context_processors import request
from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("", views.home, name="home"),
]