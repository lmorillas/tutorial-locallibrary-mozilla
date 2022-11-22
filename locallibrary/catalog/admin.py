from django.contrib import admin
from .models import Author, Genre, Book, Language, BookInstance
from django.utils.translation import gettext_lazy as _


admin.site.site_header = _("Local Library Admin Site")
admin.site.site_title = _("Local Library Portal")
admin.site.index_title = _("Welcome to Local Library Admin Site")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('genre',)
    search_fields = ('title', 'author__first_name', 'author__last_name')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status_color', 'img_image')
    list_filter = ('status', 'due_back')
