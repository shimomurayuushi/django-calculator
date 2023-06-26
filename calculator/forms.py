from django import forms

class CalcPlusForm(forms.Form):
    val1 = forms.FloatField(label='高さの値(高い方)')
    val2 = forms.FloatField(label='高さの値')
    val3 = forms.FloatField(label='横幅(長い方)')
    val4 = forms.FloatField(label='横幅')