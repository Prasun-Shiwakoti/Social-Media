# Generated by Django 4.0.4 on 2022-05-18 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainWebsite', '0015_detaileduser_chats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detaileduser',
            name='chats',
            field=models.JSONField(default=dict),
        ),
    ]
