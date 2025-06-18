from django.urls import path
from . import views

urlpatterns = [
    path('', views.registro), # Esto hace que la raíz muestre el formulario
    path('registro/', views.registro, name='registro'),
]