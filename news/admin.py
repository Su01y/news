from django.contrib import admin

from .models import News, Tags


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    save_as = True


class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(News, NewsAdmin)
admin.site.register(Tags, TagsAdmin)
