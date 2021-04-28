from django.db import models

# Create your models here.


class My_Album(models.Model):
    thumbnail = models.ImageField(upload_to='my_album/photo/')
    description = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)
