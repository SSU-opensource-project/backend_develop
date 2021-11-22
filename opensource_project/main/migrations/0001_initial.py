# Generated by Django 3.2.8 on 2021-11-22 11:05

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=main.models.upload_to_func)),
                ('thumname_image', models.ImageField(blank=True, upload_to='')),
                ('comment', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
