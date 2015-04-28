from django.forms import ModelForm
from gambler.models import Partido, Apuesta

class PartidoForm(ModelForm):
    class Meta:
        model = Partido
        exclude = ('user', 'date',)

class ApuestaForm(ModelForm):
    class Meta:
        model = Apuesta
        exclude = ('partido', 'user', 'date',)