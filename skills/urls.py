# you can use from .import views also
from django.urls import path
from skills import views
urlpatterns = [
  
 path('',views.sindex ,name="skillshow"),
    
]
