from django.urls import path
from . import views
urlpatterns = [
    path('', views.inversionistas_view, name='inversionistas_view'),
    path('<str:pk>', views.inversionista_view, name='inversionista_view'),
]