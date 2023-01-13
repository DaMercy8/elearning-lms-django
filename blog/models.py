from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User


class Keywords(models.Model):
    class Meta():
        db_table = 'keywords'
        verbose_name_plural = "keywords"
        verbose_name = "keywords"

    name = models.TextField(max_length=50, unique=True, verbose_name=u'Search')

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=150, verbose_name="category")
    
    def __str__(self):
        return self.name


class Blog(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('header', max_length=200)
    description = models.TextField()
    blog_pic = models.ImageField(upload_to='pic_folder/', default = 'pic_folder/None/no-img.jpg', verbose_name='blogpics')
    content = RichTextUploadingField()
    created = models.DateTimeField(
            default=timezone.now)
    published = models.DateTimeField(
            blank=True, null=True)
    category = models.ManyToManyField(Category, blank=True, null=True, related_name='category')
    keywords = models.ManyToManyField(Keywords, related_name="keywordss", related_query_name="keywordss",
                                      verbose_name=u'tagss')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title



class Comments(models.Model):
    name = models.CharField(max_length=20)
    emails = models.CharField(max_length=30)
    content = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.name
