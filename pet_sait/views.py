from django.shortcuts import render
from read_dogs import DOGS, CATS , FISH


def index(request):
    return render(request, 'index.html')

def temp(request):
    return render(request, 'temp.html')

def dogs(request):
    return render(request, 'pets.html', DOGS)

def cats(request):
    return render(request, 'pets.html', CATS)

def fish(request):
    return render(request, 'pets.html', FISH)