from django.urls import path, include
from .import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_lists, name='blog_lists')
]
