from django.contrib import admin
from .models import News, Category, Tag

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'title_np', 'slug', 'publish_date', 'category', 'status')
    list_filter = ('category', 'tags', 'status')
    search_fields = ('title_en', 'title_np', 'description_en', 'description_np')
    prepopulated_fields = {'slug': ('title_en',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_np', 'slug', 'status')
    list_filter = ('status',)
    search_fields = ('name_en', 'name_np')
    prepopulated_fields = {'slug': ('name_en',)}

class TagAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_np', 'slug')
    search_fields = ('name_en', 'name_np')
    prepopulated_fields = {'slug': ('name_en',)}

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)