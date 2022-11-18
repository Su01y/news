# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from news.models import News
from news.serializers import NewsSerializer


class NewsAPiTestCase(APITestCase):
    def test_get(self) -> None:
        News.objects.all().delete()
        post1 = News.objects.create(title="Test post 1", content="Test content 1")
        post2 = News.objects.create(title="Test post 2", content="Test content 2")
        url = reverse("news-list")
        response = self.client.get(url)
        res = str(response.data)[-423:-3]
        serializer_data = str(NewsSerializer([post1, post2], many=True).data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, res)

    def test_status(self) -> None:
        url = reverse("news-list")
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_detail(self) -> None:
        News.objects.all().delete()
        post = News.objects.create(title="Test post", content="Test content")
        url = "/api/v1/news/1"
        response = self.client.get(url)
        serializer_data = NewsSerializer(post).data
        self.assertEqual(response.data, serializer_data)
