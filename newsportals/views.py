from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import News, Category, Tag
from .forms import NewsForm

def index(request):
    return render(request,'index.html')

def news_list(request):
    news = News.objects.filter(status='active')
    context = {'news': news}
    return render(request, 'news/news_list.html', context)

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    context = {'news': news}
    return render(request, 'news/news_detail.html', context)

def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            form.save_m2m()  # Save many-to-many relationships
            return redirect('news_detail', slug=news.slug)
    else:
        form = NewsForm()
    context = {'form': form}
    return render(request, 'news/news_form.html', context)