# Generated by Django 3.2.4 on 2021-08-18 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_alter_image_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]