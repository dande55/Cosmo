"""
Definition of views.
"""
from django.shortcuts import render
from app import forms
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.db import models
from .models import Blog
from .models import Comment # использование модели комментариев
from .forms import CommentForm # использование формы ввода комментария

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    posts = Blog.objects.all() # запрос на выбор всех статей блога из модели
    last_pages = Blog.objects.order_by("-id")[0:4]
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'posts': posts, # передача списка статей в шаблон веб-страницы
            'last_pages': last_pages,
            'year':datetime.now().year,
        }
    )


def blog(request):

    """Renders the blog page."""

    assert isinstance(request, HttpRequest)

    posts = Blog.objects.all() # запрос на выбор всех статей блога из модели

    return render(

request,

'app/blog.html',

{

'title':'Блог',

'posts': posts, # передача списка статей в шаблон веб-страницы

'year':datetime.now().year,

}

)

def page(request):
    """Renders the page page."""
    assert isinstance(request, HttpRequest)
    posts = Blog.objects.all()
    return render(
        request,
        'app/page.html',
        {
            'title':'page',
            'posts' : posts,
            'year':datetime.now().year,
        }
    )

def error(request):
    """Renders the error page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/error.html',
        {
            'title':'404',
            'year':datetime.now().year,
        }
    )


def achives(request):
    """Renders the achives page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/achives.html',
        {
            'title':'achives',
            'message':'Your achives page.',
            'year':datetime.now().year,
        }
    )


def singlepage(request):
    """Renders the singlepage page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/singlepage.html',
        {
            'title':'singlepage',
            'message':'Your singlepage page.',
            'year':datetime.now().year,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )



def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def registration(request):

       """Renders the registration page."""

       if request.method == "POST": # после отправки формы

        regform = UserCreationForm (request.POST)

        if regform.is_valid(): #валидация полей формы

             reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы

             reg_f.is_staff = False # запрещен вход в административный раздел
             reg_f.is_active = True # активный пользователь

             reg_f.is_superuser = False # не является суперпользователем

             reg_f.date_joined = datetime.now() # дата регистрации
          
             reg_f.last_login = datetime.now() # дата последней авторизации

             reg_f.save() # сохраняем изменения после добавления данных

             return redirect('home') # переадресация на главную страницу после регистрации

       else:
 
             regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя

             assert isinstance(request, HttpRequest)

             return render(

                    request,

                    'app/registration.html',

                    {

                    'regform': regform, # передача формы в шаблон веб-страницы

                    'year':datetime.now().year,

                    }

                    )
def blogpost(request, parametr):

         """Renders the blogpost page."""

         assert isinstance(request, HttpRequest)

         post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи по параметру
         comments = Comment.objects.filter(post=parametr)
         form = CommentForm(request.POST or None)
         if request.method == "POST": # после отправки данных формы на сервер методом POST

            if form.is_valid():

                comment_f = form.save(commit=False)
                comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя
                comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату
                comment_f.post = Blog.objects.get(id=parametr) # добавляем в модель Комментария (Comment) статью, для которой данный комментарий
                comment_f.save() # сохраняем изменения после добавления полей

                return redirect('blogpost', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки комментария

            else:

                 form = CommentForm() # создание формы для ввода комментария

         return render(

         request,

         'app/blogpost.html',

         {

         'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы

         'comments': comments, # передача всех комментариев к данной статье в шаблон веб-страницы

         'form': form, # передача формы добавления комментария в шаблон веб-страницы

         'year':datetime.now().year,

         }

         )
