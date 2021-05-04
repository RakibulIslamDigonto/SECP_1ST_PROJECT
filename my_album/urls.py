from django.urls import path, include
from .import views

app_name = 'my_album'

urlpatterns = [
    path('', views.albumpage, name='albumpage'),
    path('blueberry/', views.blueberry, name='blueberry')
]
