from django.urls import path
from . import views
urlpatterns = [
    path('', views.sboempleos_view, name='sboempleos_view'),
    path('<str:pk>', views.sboempleo_view, name='sboempleo_view'),
]