from sqlite3 import Cursor
from django.shortcuts import render
import mysql.connector as sql
from django.contrib import messages
from signup.models import signup




# Create your views here.
def  signaction(request):
    if request.method=="POST":
        fname=request.POST.get('first_name',False)
        lname=request.POST.get('last_name',False)
        rno=request.POST.get('roll_no',False)
        clas=request.POST.get('class',False)
        semail=request.POST.get('email',False)
        spas=request.POST.get('password',False)
        if signup.objects.filter(email=semail).exists():
            messages.info(request,'THIS EMAIL ALREDY EXIST!!!!')
        

        else:
             ins=signup( firstname=fname,lastname=lname,rollno=rno,classs=clas,email=semail,password=spas)
             ins.save()
             messages.success(request,"Successfully Registered")
    

        
        

    return render(request,'signup_page.html')
            
