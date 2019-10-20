from django.urls import path
from .models import Post
from django.utils import timezone
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]