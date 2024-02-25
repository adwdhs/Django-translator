import json
from django.http import JsonResponse
from django.shortcuts import render
from googletrans import Translator
from django.views import View

def index(request):
    return render(request, 'index.html')

class FromText(View):
    def post(self, request):
        data = json.loads(request.body)
        txt = data
        qw = txt[:13].split(' ')
        count = len(qw[0])
        qw = qw[0].split('&')
        txt = txt[count+1::]
        trans = Translator()

        try:
            out = trans.translate(txt, src=qw[0], dest=qw[1])
        except TypeError:
            txt = ':'
            out = trans.translate(txt, src=qw[0], dest=qw[1])
        out = out.text

        return JsonResponse({'translation': out})




def transQ(request):
    q = request.GET.get('q', '')
    context = {
        'q': q,

    }

    return render(request, 'index.html', context)

def transQW(request):
    q = request.GET.get('q', '')
    w = request.GET.get('w', '')
    context = {
        'q': q,
        'w': w
    }
    print(q, w)
    return render(request, 'index.html', context)

