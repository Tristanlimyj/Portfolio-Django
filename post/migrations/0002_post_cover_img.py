# Generated by Django 3.1.4 on 2020-12-10 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover_img',
            field=models.ImageField(default='', upload_to='post_cover_img'),
            preserve_default=False,
        ),
    ]
