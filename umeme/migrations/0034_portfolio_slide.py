# Generated by Django 5.0.7 on 2024-12-04 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umeme', '0033_portfolio_desc_portfolio_head'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='slide',
            field=models.CharField(default='', max_length=50),
        ),
    ]
