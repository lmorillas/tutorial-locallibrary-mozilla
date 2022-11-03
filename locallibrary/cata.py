from catalog.models import Book

for b in Book.objects.all():
    print(b)


