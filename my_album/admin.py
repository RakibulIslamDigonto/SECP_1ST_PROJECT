from django.contrib import admin
from .models import My_Album

# Register your models here.


class AlbumAdmin(admin.ModelAdmin):
    list_display = [
        'thumbnail',
        'description',
        'creation'
    ]


admin.site.register(My_Album, AlbumAdmin)
