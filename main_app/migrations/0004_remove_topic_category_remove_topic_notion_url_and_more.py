# Generated by Django 4.1 on 2022-08-11 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_topic_youtube_url_alter_topic_notion_url'),
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