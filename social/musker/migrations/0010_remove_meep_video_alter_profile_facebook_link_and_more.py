# Generated by Django 4.2.7 on 2023-12-06 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musker', '0009_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meep',
            name='video',
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='homepage_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkedin_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
