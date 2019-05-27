#coding:utf-8
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
def home (request):
    #return HttpResponse (u'Привет мир!',mimetype="text/plain")
    #return render(request,'index.html',{})
    return render(request,'static_handler.html',{})
