# Generated by Django 4.2.4 on 2023-09-28 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_itemvariant_size_alter_orderitem_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemvariant',
            name='image',
        ),
        migrations.RemoveField(
            model_name='itemvariant',
            name='price',
        ),
        migrations.RemoveField(
            model_name='itemvariant',
            name='quantity',
        ),
    ]