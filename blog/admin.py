from django.contrib import admin
from .models import *
from ckeditor.fields import RichTextField

class BlogAdmin(admin.ModelAdmin):
    body = RichTextUploadingField()
    filter = ( 'title')
    search_fields = ['title']
    list_display = ['title','author','published']
    list_filter = ['created']
    
    class Meta:
        model = Blog



class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']


class KeywordsAdmin(admin.ModelAdmin):
    fields = ['name']



class InsertsAdmin(admin.ModelAdmin):
    field = ['nazvanie']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Keywords, KeywordsAdmin)
admin.site.register(Comments)

