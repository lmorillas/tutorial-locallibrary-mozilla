# urls de nuestra aplicación catalogo
from django.urls import path
from .views import index, acerca_de

urlpatterns = [
    path('', index, name='index'),
    path('acerca-de/', acerca_de, name='acercade'),
]