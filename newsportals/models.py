from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name_en = models.CharField(max_length=100)
    name_np = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    status = models.BooleanField(default=True)  # True for active, False for inactive

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_en)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name_en

class Tag(models.Model):
    name_en = models.CharField(max_length=100)
    name_np = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_en)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name_en

class News(models.Model):
    title_en = models.CharField(max_length=200)
    title_np = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    publish_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    description_en = models.TextField()
    description_np = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    status = models.BooleanField()  # True for active, False for inactive

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title_en)
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title_en