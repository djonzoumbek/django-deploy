from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'hello-word.html')


def healthz_check(request):
    return HttpResponse('ok')