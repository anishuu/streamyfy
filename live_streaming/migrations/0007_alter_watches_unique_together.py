# Generated by Django 5.0.3 on 2024-03-26 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('live_streaming', '0006_alter_watches_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='watches',
            unique_together=set(),
        ),
    ]