# Generated by Django 3.1.2 on 2020-10-11 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20201010_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='date_log',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
