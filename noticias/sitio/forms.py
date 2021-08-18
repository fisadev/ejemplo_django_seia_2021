from django import forms

from django.core.exceptions import ValidationError


class FormContacto(forms.Form):
    asunto = forms.CharField(max_length=125)
    texto = forms.CharField(max_length=500)
    email = forms.EmailField(max_length=125)
    password = forms.CharField(widget=forms.PasswordInput())


    def clean_texto(self):
        texto_ingresado = self.cleaned_data['texto']
        if "maldito" in texto_ingresado:
            raise ValidationError("No se puede putear")

        return texto_ingresado + " (no tenía puteadas)"
