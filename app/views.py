from django.shortcuts import render
from .models import Book
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def home(request):
    if request.method=="POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        person = request.POST.get('person')
        date = request.POST.get('date')
        data = Book(name=name,number=number,email=email,person=person,date=date)
        data.save()
    
    return render(request,'index.html')
def menu(request):
    return render(request,'menu.html')
def about(request):
    return render(request,'about.html')
def book(request):
    
  
  return render(request,'book.html')
