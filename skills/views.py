from django.shortcuts import render

# Create your views here.
def sindex(request):
    services = {"services":"active"}
    return render(request,"skills/sindex.html",services)