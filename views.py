import email
from sqlite3 import Cursor
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
import mysql.connector as sql
from signup.models import signup


# Create your views here.
def  loginaction(request):
    
    if request.method=="POST":
        lemail=request.POST.get('email',False)
        lpsw=request.POST.get('password',False)
        if (lemail=='jk@gmail.com'and lpsw=='12345678'):
            return redirect('http://localhost:8000/adminpage/')
        else:
            if signup.objects.filter(email=lemail).exists() and signup.objects.filter(password=lpsw).exists():
                request.session['email']=lemail
                
                return redirect('http://localhost:8000/user/')
            else:
                 messages.success(request,"please enter correct password")



            

    return render(request,'login_page.html')
            