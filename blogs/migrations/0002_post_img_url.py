# Generated by Django 4.1.3 on 2022-12-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_url',
            field=models.TextField(default='no image provided'),
        ),
    ]
