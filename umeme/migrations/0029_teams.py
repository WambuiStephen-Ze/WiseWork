# Generated by Django 5.0.7 on 2024-12-04 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umeme', '0028_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField()),
            ],
        ),
    ]
