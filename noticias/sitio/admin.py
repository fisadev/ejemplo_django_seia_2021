from django.contrib import admin

# Register your models here.
from sitio.models import Noticia, Categoria

@admin.register(Noticia)
class AdminNoticia(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha', 'categoria', 'estado')
    list_filter = ('archivada', 'fecha', 'categoria', 'estado')
    search_fields = ('texto', )
    date_hierarchy = 'fecha'


@admin.register(Categoria)
class AdminCategoria(admin.ModelAdmin):
    list_display = ('id', 'nombre')


