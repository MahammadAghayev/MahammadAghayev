# Generated by Django 4.2.6 on 2023-12-10 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_productitem_order_productitem_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
