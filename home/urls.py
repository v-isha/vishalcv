from django.urls import path 
from home import views
urlpatterns = [
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('contactus/',views.contactus,name="contactus"),
    # path('login/',views.login,name="login"),
]
