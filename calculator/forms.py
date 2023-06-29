from django import forms

from .models import Calculator


class CalcForm(forms.ModelForm):
    class Meta:
        model = Calculator
        fields = {'val1', 'val2', 'val3', 'val4'}
        labels = {'val1': '高さ(長い方)', 'val2': '高さ', 'val3': '横幅(長い方)', 'val4': '横幅'}