# Generated by Django 5.0.1 on 2024-02-10 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_postcontent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcontent',
            old_name='Author',
            new_name='author',
        ),
        migrations.AddField(
            model_name='postcontent',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
