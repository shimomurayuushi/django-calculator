from django.shortcuts import render
from .forms import CalcPlusForm
import numpy as np



def index(request):
    params = {
        'title': 'Calculator45',
        'forms': CalcPlusForm(),
        'Answer': 'Answer is '
    }
    if (request.method == 'POST'):
        cal1 = np.square(float(request.POST['val1']) - float(request.POST['val2']))
        cal2 = np.square(float(request.POST['val3']) - float(request.POST['val4']))
        params['answer'] = '芯引き前の寸法 ' + str(np.sqrt(cal1 + cal2) * 1.4) 
        params['forms'] = CalcPlusForm(request.POST)
    return render(request, 'calculator/index.html', params)



