# Generated by Django 4.1 on 2022-08-11 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_topic_category_topic_notion_url_topic_youtube_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='category',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='notion_url',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='youtube_url',
        ),
    ]
