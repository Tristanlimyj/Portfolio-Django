# Generated by Django 3.1.4 on 2020-12-15 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20201213_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='git_repo',
            field=models.CharField(default='false', max_length=200),
        ),
    ]
