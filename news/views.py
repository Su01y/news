from typing import Any, Dict

from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .forms import NewsForm, TagsForm
from .models import News, Tags


def add_news_view(request: Any) -> Any:
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse("successfully uploaded")
    else:
        form = NewsForm()
    return render(request, "news/add_news_form.html", {"form": form})


def add_tags_view(request: Any) -> Any:
    if request.method == "POST":
        form = TagsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse("successfully uploaded")
    else:
        form = TagsForm()
    return render(request, "tags/add_tags_form.html", {"form": form})


class NewsListView(ListView):
    model = News
    template_name = "news/list.html"
    context_object_name = "posts"
    paginate_by = 2


class NewsDetailView(DetailView):
    model = News
    template_name = "news/detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        self.object.views = F("views") + 1
        self.object.save()
        self.object.refresh_from_db()
        return super().get_context_data(**kwargs)


class LikePost(DetailView):
    model = News
    template_name = "news/detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        self.object.likes = F("views") + 1
        self.object.save()
        self.object.refresh_from_db()
        return super().get_context_data(**kwargs)


class TagsListView(ListView):
    model = Tags
    template_name = "tags/list.html"
    context_object_name = "tags"


class NewsByTag(ListView):
    model = News
    template_name = "news/list.html"
    context_object_name = "posts"
    paginate_by = 2

    def get_queryset(self) -> Any:
        return News.objects.filter(tags__slug=self.kwargs["slug"])


class NewsByViews(ListView):
    model = News
    template_name = "news/list.html"
    context_object_name = "posts"
    paginate_by = 2

    def get_queryset(self) -> Any:
        return News.objects.order_by("-views")
