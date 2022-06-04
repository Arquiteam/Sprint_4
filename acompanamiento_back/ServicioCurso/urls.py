from django.urls import path
from . import views
urlpatterns = [
    path('', views.scursos_view, name='scursos_view'),
    path('<str:pk>', views.scurso_view, name='scurso_view'),
]