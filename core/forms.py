from django import forms
from .models import *


class Menform(forms.ModelForm):
    class Meta:
        model = Men
        fields = '__all__'

class Womenform(forms.ModelForm):
    class Meta:
        model = Women
        fields = '__all__'