from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello world !<h1>')

def propos(request):
    return render(request, 'blog/hello.html',{'noms':['vladmir','ahounda']})

def about(request):
    return render(request, 'blog/about.html')
# Create your views here.
