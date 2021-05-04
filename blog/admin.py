from django.contrib import admin
from .models import Blog

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'thumbnail',
        'short_description',
        'description',
        'creation'

    ]


admin.site.register(Blog, BlogAdmin)
