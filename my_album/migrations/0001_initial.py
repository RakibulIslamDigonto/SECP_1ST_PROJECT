# Generated by Django 3.2 on 2021-04-28 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='My_Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='my_album/photo/')),
                ('description', models.TextField()),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]