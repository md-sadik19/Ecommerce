from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.http import Http404
from django.db.models import Q
from django.contrib import messages

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

    contacts = Contact.objects.all().order_by('-id')

    search = request.GET.get('search')
    if search:
        contacts = Contact.objects.filter( Q(name__icontains = search) | Q(phone=search) ) 

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

def add_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        address = request.POST.get('address')

        if name and phone and age and address:
            Contact.objects.create(
                name=name,
                phone=phone,
                age=age,
                address=address  
            )
            messages.success(request, f"contact {name} added successfull")
            return redirect('contacts')
        else:
            messages.error(request, f"contact {name} not added ")

    return render(request, 'managment/add_contact.html')

def delete_contact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    messages.success(request, f"contact {contact.name} delete successful")
    return redirect('contacts')

def edit_contact(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == 'POST':
        contact_name = request.POST.get('name')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        address = request.POST.get('address')

        contact.name = contact_name
        contact.phone = phone
        contact.age = age
        contact.address = address
        contact.save()
        messages.success(request, f"contact {contact_name} updated successful")
        return redirect('contacts')

    context = {
        'contact':contact
    }
    return render(request, 'managment/edit_contact.html',context)