from typing import Any

from django.http import HttpResponse
from django.shortcuts import render

from .forms import NewsForm
from .models import News


def add_news_view(request: Any) -> Any:
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse("successfully uploaded")
    else:
        form = NewsForm()
    return render(request, "news/add_news_form.html", {"form": form})


def list_news_view(request: Any) -> Any:
    if request.method == "GET":
        news = News.objects.all()
        return render(request, "news/news_list.html", {"news": news})
