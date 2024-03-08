from django.contrib import admin
from dbapp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    emp_details=['empno','empname','empsalary','address']
admin.site.register(Employee,EmployeeAdmin)

