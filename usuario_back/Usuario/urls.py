from django.urls import path
from . import views

app_name ="usuario"
urlpatterns = [
    path('', views.usuarios_view, name='usuarios_view'),
    path('<str:pk>', views.usuario_view, name='usuario_view'),
    path('registro/', views.registro, name='registro'),
    path('ingreso/', views.ingreso, name='ingreso'),
    path('estudiante/<str:pk>', views.estudiante, name='estudiante'),
    path('inversionista/<str:pk>', views.inversionista, name='inversionista'),
]