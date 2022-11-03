from typing import Any

from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, verbose_name="url", unique=True, null=True)
    photo = models.ImageField(
        upload_to="images/",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=["jpg"])],
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    content = models.TextField(max_length=10000, blank=True, null=True)
    likes = models.IntegerField(default=0)
    tags = models.ManyToManyField("Tags", blank=True, related_name="news")
    views = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "New"
        ordering = ["-title"]

    def get_absolute_url(self) -> Any:
        return reverse("post", kwargs={"slug": self.slug})


class Tags(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name="url", unique=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Tag"
        ordering = ["title"]

    def get_absolute_url(self) -> Any:
        return reverse("tag", kwargs={"slug": self.slug})
