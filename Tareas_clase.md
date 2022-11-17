## Tareas clase

* Revisar que los modelos sean correctos
* Poner en marcha el servidor
* Revisar que las páginas del día anterior se ven bien
* Crear objetos usando fixtures
> Tienes que copiar el archivo `catalogo.json` dentro de la carpeta `catalog/fixtures` 
`python manage.py loaddata catalogo`
* Lanzar consultas en la consola
```bash
python manage.py shell
```
```python
from catalog.models import Book

Book.objects.all()
Book.objects.all()[:5]
Book.objects.all().order_by('-id')[:5]
Book.objects.filter(title='1984')
```
* Modificar vista inicial `index` (`catalog\views.py`) para que muestre los últimos 5 libros como una lista

* Activar el admin para `Book, Author, Genre, Language`

>  Tienes que tener un superusuario para acceder al admin (`python manage.py createsuperuser`)


## Mejoras propestas
* Mapa en contacto
* Crear formulario de contacto (por email o guardando en base de datos)
  * Ventajas e inconvenientes?
  * Ejemplos: 
      * https://ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend
      * https://www.valentinog.com/blog/django-widgets/
* Buscador para autores
* Mensajes de éxito al guardar y modificar.
   * https://ordinarycoders.com/blog/article/django-messages-framework
   * https://diegoamorin.com/django-messages-framework/
* Confirmación de **deleteView** en ventana modal.

* Gestión de permisos y autenticación
* Automatización de extracción/inserción de datos