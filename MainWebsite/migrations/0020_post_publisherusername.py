# Generated by Django 4.0.4 on 2022-05-19 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainWebsite', '0019_alter_post_likers'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='PublisherUsername',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
