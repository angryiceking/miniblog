# Generated by Django 2.2.13 on 2021-03-21 12:09

import datetime
from django.db import migrations
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_content',
            field=tinymce.models.HTMLField(default=datetime.datetime(2021, 3, 21, 12, 9, 22, 794681, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
