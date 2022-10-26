from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import add_news_view, list_news_view

urlpatterns = [path("add news", add_news_view), path("news list", list_news_view)]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
