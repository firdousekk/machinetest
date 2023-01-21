from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'home_templates/index.html')

def about(request):
    return render(request,'home_templates/about.html')

def trophies(request):
    return render(request,'home_templates/trophies.html')

def players(request):
    return render(request,'home_templates/players.html')    

def formexm(request):
    return render(request,'home_templates/formexm.html')    

def loginexm(request):
    return render(request,'home_templates/loginexm.html')   

def homeexm(request):
    return render(request,'home_templates/homeexm.html')    
