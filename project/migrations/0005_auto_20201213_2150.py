# Generated by Django 3.1.4 on 2020-12-13 13:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20201213_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]