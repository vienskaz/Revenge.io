# Generated by Django 4.2.4 on 2023-09-28 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_itemvariant_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemvariant',
            name='size',
            field=models.CharField(blank=True, choices=[('SMALL', 'SMALL'), ('MEDIUM', 'MEDIUM'), ('LARGE', 'LARGE'), ('XLARGE', 'XLARGE'), ('XXLARGE', 'XXLARGE'), ('OS', 'OS')], default='OS', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.itemvariant'),
        ),
    ]
