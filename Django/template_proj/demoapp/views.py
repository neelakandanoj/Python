from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def display(request):
    date=datetime.datetime.now()
    Hour=int(date.strftime('%H'))
    msg=''
    if Hour<12:
        msg+='Good Morning'
    else:
        msg+='Good Evening'
    date_dic={'display_date':date,'name':'Neela','Hour':msg}
    return render(request,'demoapp/home.html',context=date_dic)

