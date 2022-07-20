from django import forms


class NuevoPipeta(forms.Form):
    tipo = forms.CharField (max_length= 30)
    nombre = forms.CharField (max_length=30)
    peso = forms.IntegerField(min_value=0)
    precio = forms.IntegerField(min_value=0)

class NuevoComida (forms.Form):
    tipo = forms.CharField (max_length= 30)
    tamaño = forms.CharField (max_length= 30)
    nombre = forms.CharField (max_length=30)
    peso = forms.IntegerField(min_value=0)
    precio = forms.IntegerField(min_value=0)

class NuevoCollar (forms.Form):
    largo = forms.IntegerField(min_value=0)
    color = forms.CharField (max_length=30)
    precio = forms.IntegerField(min_value=0)

class NuevoBlogCard (forms.Form):
    título = forms.CharField (max_length= 30)
    subtítulo = forms.CharField (max_length= 30)
    texto = forms.CharField (max_length=1000)
    imagen = forms.CharField (max_length=1000)
    