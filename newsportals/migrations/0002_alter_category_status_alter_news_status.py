# Generated by Django 5.0.4 on 2024-05-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsportals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
