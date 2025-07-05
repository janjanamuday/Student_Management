from django.contrib import admin
from .models import student
# Register your models here.


class studentAdmin(admin.ModelAdmin):
    list_display=('id','name','email','age','gender',)
    list_display_links=('id','name',)





admin.site.register(student)