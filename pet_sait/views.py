from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def temp(request):
    return render(request, 'temp.html')

def pets(request):
    return render(request, 'pets.html')