# Generated by Django 4.2.7 on 2023-12-06 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musker', '0007_meep_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meep',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='meep_videos/'),
        ),
    ]