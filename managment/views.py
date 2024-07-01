from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import Http404

# Create your views here.
def home(request):
    people = [
        {
        "name": "jafae sadik",
        "age": 21,
        "number": "01642625416"
        },
        {
        "name": "Ayman sadik",
        "age": 21,
        "number": "01642625416"
        },
        {
        "name": "Tasfir Ahmed",
        "age": 21,
        "number": "01642625416"
        }
    ]

    return render(request, 'managment/home.html')

def contacts(request):

    contacts = Contact.objects.all()

    context = {
        'contacts':contacts
    }

    return render(request, 'managment/contacts.html',context)

def detail(request, id):
    
    contact = Contact.objects.filter(id=id).first
    
    
    context = {
        'contact':contact
    }
    return render(request,'managment/detail.html',context)

def about(request):
    return render(request, 'managment/about.html')