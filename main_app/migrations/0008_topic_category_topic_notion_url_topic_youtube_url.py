# Generated by Django 4.1 on 2022-08-11 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_topic_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='category',
            field=models.CharField(default='Computer Science', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='notion_url',
            field=models.CharField(default='https://www.notion.so/seiremote/SEI-Remote-5-23-76818627ae2d4764963bf1fe86a6b1c3', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='youtube_url',
            field=models.CharField(default='https://www.youtube.com/channel/UCUuibJM8qV3Y6WoNCetWvRQ', max_length=250),
            preserve_default=False,
        ),
    ]
