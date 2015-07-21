from django import forms

from hoteles.models import Ciudad

class CiudadForm(forms.ModelForm):

    class Meta:
        model = Ciudad
        fields = ('nombre',)