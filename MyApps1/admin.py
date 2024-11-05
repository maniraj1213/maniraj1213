from django.contrib import admin
from django.db import  models
from MyApps1.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eadd']

admin.site.register(Employee,EmployeeAdmin)

