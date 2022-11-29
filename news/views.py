from rest_framework import filters, generics

from .models import News
from .serializers import NewsSerializer


class NewsListView(generics.ListAPIView):
    serializer_class = NewsSerializer
    ordering_fields = ["likes", "views"]
    queryset = News.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering = ["created_at"]


class NewsDetailView(generics.RetrieveAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
