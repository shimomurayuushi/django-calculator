import numpy as np

from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import Calcu45, Calculator
from .forms import CalcForm, Calcu45Form


class Topview(TemplateView):
    template_name = 'calculator/top.html'
    

class CalculatorView(View):
    template_name = 'calculator/index.html'
    form_class = CalcForm

    def get(self, request):
        forms = self.form_class()
        params = {
            'title': 'Calculator45',
            'forms': forms,
            'Answer': '',
            'interim': '',
        }
        return render(request, self.template_name, params)

    def post(self, request):
        forms = self.form_class(request.POST)
        params = {
            'title': 'Calculator45',
            'forms': forms,
            'Answer': '',
            'interim': '',
        }
        if forms.is_valid():
            cal1 = np.square(float(forms.cleaned_data['val1']) - float(forms.cleaned_data['val2']))
            cal2 = np.square(float(forms.cleaned_data['val3']) - float(forms.cleaned_data['val4']))
            cal3 = np.sqrt(cal1 + cal2)
            params['answer'] = '芯引き前の寸法: ' + str(cal3 * 1.4)
            params['interim'] = '1.4かける前の寸法: ' + str(cal3)
        return render(request, self.template_name, params)


class CalcuView(View):
    template_name = 'calculator/calcu45.html'
    model = Calcu45
    form_class = Calcu45Form

    def get(self, request):
        forms = self.form_class()
        params = {
            'title': 'Calcu45',
            'forms': forms,
            'Answer': '',
        }
        return render(request, self.template_name, params)

    def post(self, request):
        forms = self.form_class(request.POST)
        params = {
            'title': 'Calcu45',
            'forms': forms,
            'Answer': '',
        }
        if forms.is_valid():
            width = forms.cleaned_data['width']
            calc_result = width * 1.4
            params['Answer'] = '芯引き前の寸法: ' + str(calc_result)
        return render(request, self.template_name, params)




