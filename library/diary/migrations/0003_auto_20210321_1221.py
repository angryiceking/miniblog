# Generated by Django 2.2.13 on 2021-03-21 12:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20210321_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]