# Generated by Django 5.0.7 on 2024-12-03 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umeme', '0012_status_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bgt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
