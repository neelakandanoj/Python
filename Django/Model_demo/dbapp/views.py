from django.shortcuts import render
from dbapp.models import Employee
# Create your views here.
def empdetail(request):

    data=Employee.objects.all()
    emp_dic={'emp_list':data}
    return render(request,'dbapp/index.html',context=emp_dic)