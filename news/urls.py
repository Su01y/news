# from django.conf import settings
# from django.conf.urls.static import static
# from django.urls import include, path
# from rest_framework import routers

from django.urls import path

from .views import NewsDetailView, NewsListView

# from django.urls import include

# router = routers.DefaultRouter()
# router.register(r'news', NewsViewSet, basename='news')

# urlpatterns = [
#     path("add news", add_news_view),
#     path("add tags", add_tags_view),
#     path("news", NewsListView.as_view(), name="news"),
#     path("tags", TagsListView.as_view(), name="tags"),
#     path("news/<str:slug>/", NewsDetailView.as_view(), name="post"),
#     path("views", NewsByViews.as_view(), name="post_by_views"),
#     path("tag/<str:slug>/", NewsByTag.as_view(), name="tag"),
# ]

urlpatterns = [
    path("api/v1/news/", NewsListView.as_view()),
    path("api/v1/news/<int:pk>", NewsDetailView.as_view()),
    # path('api/v1/views/', NewsByViewsListView.as_view()),
    # path('api/v1/', include(router.urls)),
]

# if settings.DEBUG:

#     urlpatterns = [
#         path('__debug__/', include('debug_toolbar.urls'))
#     ] + urlpatterns
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
