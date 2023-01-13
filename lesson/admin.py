from django.contrib import admin
from .models import Lesson,Video,Audio

# Register your models here.

admin.site.register(Lesson)
admin.site.register(Video)
admin.site.register(Audio)
