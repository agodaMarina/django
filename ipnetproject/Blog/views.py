from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Blog.models import Articles
from Blog.forms import ContactForm
from Blog.forms import ArticleForm
from django.core.mail import send_mail


def hello(request):
    return HttpResponse('<h1>Hello world !<h1>')


def propos(request):
    return render(request, 'blog/hello.html', {'noms': ['vladmir', 'ahounda']})


def about(request):
    return render(request, 'blog/about.html')


def email_sent(request):
    return render(request, 'blog/email_sent.html')


def contact(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():
            send_mail(

                subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return HttpResponseRedirect('/email_sent/')
    else:
        form = ContactForm()

        return render(request,
                      'blog/contact.html',
                      {'form': form})


def article(request):
    articles = Articles.objects.all()
    return render(request, 'blog/article.html', {'articles': articles})


def article_detail(request, id):
    articles = Articles.objects.get(id=id)
    return render(request, 'blog/articledetail.html', {'articles': articles})


# fonction pouur le create
def article_create(request):
    if (request.method == 'POST'):

        form = ArticleForm(request.POST)

        if (form.is_valid()):
            form.save()

            return HttpResponseRedirect('/article/')

    else:
        form = ArticleForm()

        return render(request, 'blog/create.html', {'form': form})


# fonction pour l'update
def article_update(request, id):
    article = Articles.objects.get(id=id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/article/{id}/')
    else:
        form = ArticleForm(instance=article)

    return render(request,
                  'blog/article_update.html',
                  {'form': form})
