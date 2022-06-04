from django.urls import path
from . import views
urlpatterns = [
    path('', views.sedcontinuas_view, name='sedcontinuas_view'),
    path('<str:pk>', views.sedcontinua_view, name='sedcontinua_view'),
]