# Generated by Django 4.0.4 on 2022-05-15 06:58

import MainWebsite.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainWebsite', '0007_post_publisherimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Comments',
            field=models.JSONField(default=MainWebsite.models.defaultJsonValue),
        ),
    ]
