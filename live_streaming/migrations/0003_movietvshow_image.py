# Generated by Django 5.0.3 on 2024-03-23 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_streaming', '0002_alter_payment_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='movietvshow',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='movie_images/'),
        ),
    ]
