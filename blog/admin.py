from django.contrib import admin
from .models import Blog, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class BlogAdmin(SummernoteModelAdmin):
    list_display = [
        'title',
        'short_description',
        'description',
        'thumbnail'
    ]

    summernote_fields = ('description',)


admin.site.register(Blog, BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'body'

    ]


admin.site.register(Comment, CommentAdmin)
