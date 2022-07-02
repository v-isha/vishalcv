from django.contrib import admin
from . models import Contactus
# Register your models here.

@admin.register(Contactus)
class ConatctAdmin(admin.ModelAdmin):
    list_display = ("name","email","mobile","remark")