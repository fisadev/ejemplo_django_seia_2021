from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    ESTADOS = (
        ('publicada', 'Noticia publicada en el sitio'),
        ('borrador', 'Noticia todavía siendo escrita'),
        ('en_revision', 'Noticia siendo revisada'),
    )
    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    archivada = models.BooleanField(default=False)
    denuncias = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, choices=ESTADOS, default="borrador")
