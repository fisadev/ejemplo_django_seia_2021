from django.shortcuts import render, redirect

from sitio.models import Noticia
from sitio.forms import FormContacto
from datetime import datetime



def inicio(request):
    nueva = Noticia()
    nueva.titulo = 'entro alguien!'
    nueva.texto = 'acaba de entrar alguien al sitio'
    nueva.fecha = datetime.now()
    nueva.save()

    noticias = Noticia.objects.filter(archivada=False).order_by('fecha')
    return render(request, 'inicio.html', {'lista_noticias': noticias})


def ejemplo_form_pelado(request):
    if request.method == "GET":
        print("Me pidieron el form, no hago nada raro")
    else:
        print("En request.GET llegó esto:")
        print(request.GET)
        print("En request.POST llegó esto:")
        print(request.POST)

        nueva = Noticia()
        nueva.titulo = 'Alguien consultó algo!'
        nueva.texto = request.POST["texto"]
        nueva.fecha = datetime.now()
        nueva.save()

    return render(request, 'ejemplo_form_pelado.html', {})



def ejemplo_form_django(request):
    if request.method == "POST":
        form = FormContacto(request.POST)

        if form.is_valid():
            nueva = Noticia()
            nueva.titulo = 'Alguien consultó algo!'
            nueva.texto = form.cleaned_data["texto"]
            nueva.fecha = datetime.now()
            nueva.save()

            return redirect("inicio")
    else:
        form = FormContacto()

    return render(request, 'ejemplo_form_django.html', {'form': form})



