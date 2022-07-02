from django.shortcuts import render

# Create your views here.
def education(request):
    education = {"skill":"active"}
    return render(request,"education/edu.html",education)