# Generated by Django 4.0.4 on 2022-05-19 11:21

import MainWebsite.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainWebsite', '0018_post_likers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Likers',
            field=models.JSONField(default=MainWebsite.models.defaultChatValue),
        ),
    ]
