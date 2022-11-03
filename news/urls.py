# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path

from .views import (
    NewsByTag,
    NewsByViews,
    NewsDetailView,
    NewsListView,
    TagsListView,
    add_news_view,
    add_tags_view,
)

# from django.urls import include

urlpatterns = [
    path("add news", add_news_view),
    path("add tags", add_tags_view),
    path("news", NewsListView.as_view(), name="news"),
    path("tags", TagsListView.as_view(), name="tags"),
    path("news/<str:slug>/", NewsDetailView.as_view(), name="post"),
    path("views", NewsByViews.as_view(), name="post_by_views"),
    path("tag/<str:slug>/", NewsByTag.as_view(), name="tag"),
]

# if settings.DEBUG:

#     urlpatterns = [
#         path('__debug__/', include('debug_toolbar.urls'))
#     ] + urlpatterns
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
