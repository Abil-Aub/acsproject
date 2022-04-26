from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('api/<pin>/', views.api_get_address),
    path('info/', views.info)
]
