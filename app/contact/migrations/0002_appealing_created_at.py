# Generated by Django 4.2.6 on 2023-11-29 23:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appealing',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
