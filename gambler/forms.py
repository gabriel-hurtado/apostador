from django.forms import ModelForm
from gambler.models import Apuesta

class ApuestaForm(ModelForm):
    class Meta:
        model = Apuesta
        exclude = ('partido', 'user', 'date',)