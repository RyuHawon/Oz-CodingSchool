"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, Http404


movie_list = [
    {'title': '프로젝트 헤일메리', 'director': '크리스 밀러'},
    {'title': '왕과 사는 남자', 'director': '장항준'},
    {'title': '호퍼스', 'director': '다니엘 총'},
    {'title': '메소드연기', 'director': '이기혁'},
]


def index(request):
    return HttpResponse("<h1>hello</h1>")


def book_list(request):

    book_text = ''

    for i in range(0, 10):
        book_text += f'book {i}<br>'

    return HttpResponse(book_text)


def book(request, num):
    book_text = f'book {num}번 페이지입니다.'
    return HttpResponse(book_text)


def language(request, lang):
    return HttpResponse(f'<h1>{lang} 언어 페이지입니다.</h1>')


def movies(request):
    movie_titles = [
        f'<a href="/movie/{index}/">{movie['title']}</a>'
        for index, movie in enumerate(movie_list)
    ]

    response_text = '<br>'.join(movie_titles)

    return HttpResponse(response_text)


def movie_detail(request, index):
    if index > len(movie_list) - 1:
        raise Http404

    movie = movie_list[index]

    response_text = f'<h1>{movie['title']}</h1> <p>감독: {movie['director']}</p>'
    return HttpResponse(response_text)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('book_list/', book_list),
    path('book_list/<int:num>/', book),
    path('language/<str:lang>/', language),
    path('movie/', movies),
    path('movie/<int:index>/', movie_detail),
]
