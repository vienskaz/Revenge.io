# Generated by Django 4.2.4 on 2023-09-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_remove_itemvariant_image_remove_itemvariant_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemvariant',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to='images'),
        ),
    ]
