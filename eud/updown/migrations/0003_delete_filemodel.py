# Generated by Django 3.1.2 on 2020-10-26 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('updown', '0002_remove_filemodel_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FileModel',
        ),
    ]
