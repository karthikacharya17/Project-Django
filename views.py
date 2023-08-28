from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
from signup.models import signup
from signup.views import signaction

# Create your views here.
def  regaction(request):
        k1 = signup.objects.all()
        context = {'signup':k1}
        
        return render(request,'reguser.html',context)


