from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from.models import Book
# Create your views here.

@login_required(login_url='login')
def home(request):
    book = Book.objects.all()
    
    return render(request,'index.html',{"book":book})


@login_required(login_url='login')
def addBook(request):
    
    return render(request,'addBooks.html')

