from django.urls import path
from . import views
urlpatterns = [
    path('', views.satpsicologicas_view, name='satpsicologicas_view'),
    path('<str:pk>', views.satpsicologica_view, name='satpsicologica_view'),
]