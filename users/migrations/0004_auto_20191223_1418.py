# Generated by Django 3.0.1 on 2019-12-23 14:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191223_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimages',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2019, 12, 23, 14, 18, 0, 849194, tzinfo=utc)),
        ),
    ]
