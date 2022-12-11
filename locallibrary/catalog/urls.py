# urls de nuestra aplicación catalogo
from django.urls import path
from .views import index, acerca_de, BookListView, BookDetailView, \
        SearchResultsListView, LibrosPrestados, renovar_libro, \
        AuthorCreate, AuthorUpdate, AuthorDelete, AuthorListView, \
        BookUpdateView
    

urlpatterns = [
    path('', index, name='index'),
    path('acerca-de/', acerca_de, name='acercade'),
    path('libros/', BookListView.as_view(), name='lista-libros'),
    path('libros/<int:pk>', BookDetailView.as_view(), name='detalle-libro'),
    path('libros/<int:pk>/update', BookUpdateView.as_view(), name='editar-libro'),
    path('busqueda/', SearchResultsListView.as_view(), name='buscar'),
    path('prestados/', LibrosPrestados.as_view(), name='prestados'),
    path('libro/<uuid:pk>/renovar/', renovar_libro, name='renovar-fecha'),
    path('autores/', AuthorListView.as_view(), name='autores'),
    path('autores/create/', AuthorCreate.as_view(), name='author-create'),
    path('autores/<int:pk>/update/', AuthorUpdate.as_view(), name='author-update'),
    path('autores/<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),


]