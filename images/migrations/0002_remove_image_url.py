# Generated by Django 3.2.4 on 2021-07-15 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='url',
        ),
    ]
