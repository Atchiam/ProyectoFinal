from django import forms


class NuevoBlogCard (forms.Form):
    título = forms.CharField (max_length= 30)
    subtítulo = forms.CharField (max_length= 30)
    texto = forms.CharField (max_length=1000)
    imagen = forms.CharField (max_length=1000)
    