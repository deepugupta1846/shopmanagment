# Generated by Django 3.1.6 on 2021-02-11 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210211_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopmanagment',
            name='Company',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='shopmanagment',
            name='Type',
            field=models.CharField(default='', max_length=50),
        ),
    ]
