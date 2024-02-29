from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish(request):
    msg="<h1>Hi Learning Django</h1>"
    return HttpResponse(msg)
