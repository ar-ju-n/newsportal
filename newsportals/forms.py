from django import forms
from .models import News, Category, Tag

class NewsForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = News
        fields = ['title_en', 'title_np', 'publish_date', 'category', 'tags', 'description_en', 'description_np', 'image', 'status']