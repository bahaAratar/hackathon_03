# Generated by Django 4.1.7 on 2023-02-21 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
