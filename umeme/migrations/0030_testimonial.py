# Generated by Django 5.0.7 on 2024-12-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umeme', '0029_teams'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
