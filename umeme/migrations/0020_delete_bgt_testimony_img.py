# Generated by Django 5.0.7 on 2024-12-03 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umeme', '0019_remove_bgt_filtered_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bgt',
        ),
        migrations.AddField(
            model_name='testimony',
            name='img',
            field=models.ImageField(default='none', upload_to='images/'),
        ),
    ]