from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'product/home.html')

def contact(request):
    return render(request, 'product/contact.html')

def about(request):
    return HttpResponse("Product about page")
