# Generated by Django 3.1.6 on 2021-02-10 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopmanagment',
            old_name='item',
            new_name='Item_Name',
        ),
        migrations.RenameField(
            model_name='shopmanagment',
            old_name='rate',
            new_name='Rate',
        ),
    ]
