from django.shortcuts import render
from django.shortcuts import redirect 
from .models import Name

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello Django!!!")

def myyear(request):
    return HttpResponse("hello Django!!!")

def year(request):
    return HttpResponse("hello Django!!!")

def name(request):
    return HttpResponse("hello Django!!!")

def books(request):
    ### 从models 取数传达给template 
    n = Name.objects.all()
    return render(request, 'bookslist.html', locals())