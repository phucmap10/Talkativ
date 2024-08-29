from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
    return HttpResponse('Hello World')
def index1(req):
    return HttpResponse('Child of app 1')