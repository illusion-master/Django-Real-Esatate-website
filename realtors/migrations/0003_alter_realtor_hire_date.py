# Generated by Django 3.2.6 on 2021-08-05 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_alter_realtor_hire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 8, 5, 16, 43, 11, 330933)),
        ),
    ]
