# urls de nuestra aplicación catalogo
from django.urls import path
from .views import index, acerca_de, BookListView, BookDetailView


urlpatterns = [
    path('', index, name='index'),
    path('acerca-de/', acerca_de, name='acercade'),
    path('libros/', BookListView.as_view(), name='lista-libros'),
    path('libros/<int:pk>', BookDetailView.as_view(), name='detalle-libro'),


]