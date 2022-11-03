from django import forms

from .models import News, Tags


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"


class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = "__all__"
