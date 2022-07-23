from urllib import request
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse('Hello Anmol')