from django.http import HttpResponse
from django.shortcuts import render, redirect  # redirect переадресация
from .models import Advertisement
from .forms import AdvertisementForm

from django.urls import reverse  # дает абсолютную ссылку по имени

from django.core.handlers.wsgi import WSGIRequest


def index(request):
    advertisements = Advertisement.objects.all()
    context = {
        "advertisements": advertisements
    }
    return render(request, 'advertisements/index.html', context)


def top_sellers(request):
    return render(request, 'advertisements/top-sellers.html')


def advertisement_post(request: WSGIRequest):
    print(request.method)
    print(request.POST)  # переданные данные пост запроса
    print(request.FILES)  # переданные файлы

    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)  # передаю данные на проверку
        if form.is_valid():  # проверяю правильно ли заполнены данные True
            adv = Advertisement(**form.cleaned_data)  # передаю данные в БД в виде словаря
            adv.user = request.user  # добавляю юзера из запроса
            adv.save()  # сохраняю запись
            return redirect(  # перенаправление на главную страницу
                reverse('main-page')
                # 'http://127.0.0.1:8000/'
            )

    else:  # GET или другие
        form = AdvertisementForm()  # пустая форма

    context = {"form": form}
    return render(request, 'advertisements/advertisement-post.html', context)
