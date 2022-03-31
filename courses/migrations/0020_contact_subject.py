# Generated by Django 4.0.2 on 2022-03-01 18:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default=datetime.datetime(2022, 3, 1, 18, 9, 6, 154901, tzinfo=utc), max_length=250, verbose_name='Subject'),
            preserve_default=False,
        ),
    ]
