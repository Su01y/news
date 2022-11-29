from django.urls import path

from .views import NewsDetailView, NewsListView

urlpatterns = [
    path("api/v1/news/", NewsListView.as_view(), name="news-list"),
    path("api/v1/news/<int:pk>", NewsDetailView.as_view(), name="news-detail"),
]
