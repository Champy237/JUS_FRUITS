# Generated by Django 4.2.6 on 2025-02-05 22:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='schudele_date',
            field=models.DateField(default=datetime.datetime(2025, 2, 12, 22, 8, 23, 821152)),
        ),
    ]
