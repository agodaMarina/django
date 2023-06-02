from django.shortcuts import render
from django.http import HttpResponse
from Blog.models import Articles
def hello(request):
    return HttpResponse('<h1>Hello world !<h1>')

def propos(request):
    return render(request, 'blog/hello.html',{'noms':['vladmir','ahounda']})

def about(request):
    return render(request, 'blog/about.html')
# Create your views here.
def article(request):
    articles=Articles.objects.all()
    return render(request,'blog/article.html',{'articles':articles})

def article_detail(request, id):
    articles=Articles.objects.get(id=id)
    return render(request,'blog/articledetail.html',{'articles':articles})

