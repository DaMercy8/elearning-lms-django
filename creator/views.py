from django.shortcuts import render, get_object_or_404
from .models import Creator
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


class CreateCreatorProfileView(CreateView):
    model = Creator
    fields = ('profile','bio','social-media-url')
    template_name = 'creator/creator_form.html'
    success_url = '/'


    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateCreatorProfileView, self).dispatch(*args, **kwargs)






class UpdateCreatorProfileView(UpdateView):
    model = Creator
    fields = ('profile','bio','social-media-url')
    template_name = 'creator/creator_form.html'
    success_url = '/'


    def form_valid(self,form):
        content_creator = get_object_or_404(Creator,user=self.request.user)
        form.instance.user = content_creator.user
        return super().form_valid(form)


    def get_form(self, form_class=None):
        content_creator = get_object_or_404(Creator,user=self.request.user)
        form = super(UpdateCreatorProfileView, self).get_form(form_class)
        return form

    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateCreatorProfileView, self).dispatch(*args, **kwargs)
