# Generated by Django 4.2.4 on 2023-09-28 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_item_size_itemvariant'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemvariant',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]