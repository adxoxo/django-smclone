# Generated by Django 3.2.4 on 2021-06-12 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created',
        ),
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]