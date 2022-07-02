from http.client import ImproperConnectionState
from django.shortcuts import render ,redirect
from.forms import Contactusform
from .models import Contactus
from django.contrib import messages

# Create your views here.
def home(request):
    content ={"home":"active"}
    return render(request,"home/home.html",content)
def index(request):
    return render(request,"home/index.html")    
def contactus(request):
    if request.method =="POST":
        ct =Contactusform(request.POST)
        if ct.is_valid():
            nm = ct.cleaned_data["name"]
            em = ct.cleaned_data["email"]
            mo = ct.cleaned_data["mobile"]
            rk = ct.cleaned_data["remark"]
            ct = Contactus(name=nm,email=em,mobile=mo,remark=rk)
            ct.save()
            messages.success(request, 'Congratulations!! Will contact you soon.')
            return redirect("contactus")
            
    else:
    
        ct = Contactusform()
    
    return render(request,"home/contactus.html",{"contact":"active","form":ct})    



# def login(request):

#     return render(request,"home/login.html")