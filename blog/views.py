from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from django.views import View
from .models import Blog , Category, Comments
from rest_framework import serializers
from rest_framework import viewsets, serializers
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView
)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class BlogView(ListView):
    template_name = "blog/blog.html"
    paginate_by = 10

    def get_queryset(self):
        blogs = Blog.objects.all()
        categories = Category.objects.all()

        # content = {'categories':categories,'blogs':blogs}
        return blogs

class BlogCreate(CreateView):
    model = Blog
    fields = [
		'title',
		'description',
		'blog_pic',
		'content',
		'published'
		]
    
    template_name = 'blog/blog_form.html'
    success_url = '/articles/'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BlogCreate, self).dispatch(*args, **kwargs)


class BlogUpdate(UpdateView):
    model = Blog
    fields = [
		'title',
		'description',
		'blog_pic',
		'content',
		'published'
		]
    
    template_name = 'blog/blog_form.html'
    success_url = '/articles/'


    def form_valid(self, form):

        if self.object.author == self.request.user:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BlogUpdate, self).dispatch(*args, **kwargs)


class BlogDetail(DetailView):
    model = Blog
    template_name = 'blog/blog-detail.html'