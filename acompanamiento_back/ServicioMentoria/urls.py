from django.urls import path
from . import views
urlpatterns = [
    path('', views.smentorias_view, name='smentorias_view'),
    path('<str:pk>', views.smentoria_view, name='smentoria_view'),
]