# Generated by Django 5.0.7 on 2024-12-04 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umeme', '0035_portfolio_slide1'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service',
            new_name='Skills',
        ),
        migrations.RenameModel(
            old_name='Teams',
            new_name='Time',
        ),
        migrations.RenameModel(
            old_name='Testimonial',
            new_name='Tramp',
        ),
    ]