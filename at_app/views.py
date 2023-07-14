from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')

def places(request):
    return render(request,'places.html')

def team(request):
    return render(request,'team.html')

def about(request):
    return render(request,'about_us.html')

def four(request):
    return render(request,'404.html')

def kakaria(request):
    return render(request,'kakaria.html')

def atal(request):
    return render(request,'atal_ridge.html')

def manekchok(request):
    return render(request,'manek_chowk.html')

def sidisaiyad(request):
    return render(request,'sidi_saiyad.html')

def riverfront(request):
    return render(request,'rivor_front.html')

def adalaj(request):
    return render(request,'adajaj.html')

def sabarmati(request):
    return render(request,'sabrmati_ashram.html')

def palediyam(request):
    return render(request,'palladium.html')