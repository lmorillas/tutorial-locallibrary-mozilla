from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Book

# Create your views here.
def index(request):
    texto = '''<h1>Librería Local</h1>
    <p>Esta es la página principal de la librería local.</p>'''
    # texto = 'Página inicial de la librería local'
    lista = '<h2>Mi lista de últimos libros</h2><ul>'
    # Consulta a la base de datos: últimos 5 libros
    for libro in Book.objects.all()[:5]:
        lista += f'<li>{libro.title}</li>'
    lista += '</ul>'

    return HttpResponse(texto + lista)

def acerca_de(request):
    texto = '''<h1>Acerca de</h1>
    <p>Esta es la página de acerca de de la librería local.</p>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/EZ5sIrfmSwc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    
    '''
    return HttpResponse(texto)




