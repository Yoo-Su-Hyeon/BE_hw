from django.urls import path
from . import views

app_name = 'phone'

urlpatterns = [
    path('', views.list, name='list'),
    path('result/', views.result, name='result'),
]