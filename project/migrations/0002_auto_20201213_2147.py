# Generated by Django 3.1.4 on 2020-12-13 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='git_repo',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='project_url',
            field=models.CharField(default='https://www.thealchemistalcohol.com', max_length=200),
            preserve_default=False,
        ),
    ]
