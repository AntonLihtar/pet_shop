from django.shortcuts import render
from read_dogs import DOGS


def index(request):
    return render(request, 'index.html')

def temp(request):
    return render(request, 'temp.html')

def pets(request):
    context = DOGS
    return render(request, 'pets.html', context)