from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def cu_time(request):
    time=datetime.datetime.now()
    return HttpResponse('<h1>Hi now the time is: '+ str(time)+'</h1>')
