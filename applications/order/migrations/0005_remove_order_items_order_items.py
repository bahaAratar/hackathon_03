# Generated by Django 4.1.7 on 2023-02-24 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_owner'),
        ('order', '0004_alter_order_options_alter_order_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='product.product'),
        ),
    ]