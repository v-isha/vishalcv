from django.urls import path
from education import views
urlpatterns = [
    path('education/',views.education,name="eduskills"),
    
]
