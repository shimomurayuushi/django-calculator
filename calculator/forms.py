from django import forms

from .models import Calculator, Calcu45


class CalcForm(forms.ModelForm):
    class Meta:
        model = Calculator
        fields = {'val1', 'val2', 'val3', 'val4'}
        labels = {'val1': '高さ(長い方)', 'val2': '高さ', 'val3': '横幅(長い方)', 'val4': '横幅'}


class Calcu45Form(forms.ModelForm):
    class Meta:
        model = Calcu45
        fields = {'width'}
        labels = {'width': '横幅'}