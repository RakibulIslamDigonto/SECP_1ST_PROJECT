from django.urls import path, include
from .import views

app_name = 'my_profile'

urlpatterns = [
    path('', views.homepage, name='homepage')
]
