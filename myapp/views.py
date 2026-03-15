from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {'name' : 'Alexandre'}
    return render(request, 'pages/index.html', context)

def test(request):
    return render(request, 'pages/test.html')