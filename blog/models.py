from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='my_album/photo/')
    short_description = models.TextField(max_length=300)
    description = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)
