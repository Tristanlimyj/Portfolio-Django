# Generated by Django 3.1.4 on 2020-12-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20201213_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='git_repo',
            field=models.CharField(default=False, max_length=200),
        ),
    ]
