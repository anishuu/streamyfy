# Generated by Django 5.0.3 on 2024-03-23 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_streaming', '0003_movietvshow_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movietvshow',
            name='Video',
            field=models.FileField(blank=True, null=True, upload_to='movie_videos/'),
        ),
    ]