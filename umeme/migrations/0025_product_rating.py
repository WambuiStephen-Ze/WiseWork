# Generated by Django 5.0.7 on 2024-12-03 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umeme', '0024_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]
