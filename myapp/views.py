from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import *

def filter_demo(request):
    return render(request,"filter_demo.html",{'data':"hello world",'a':10,'b':20,'num':1})