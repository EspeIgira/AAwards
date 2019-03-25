# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-25 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0007_signuprecipients'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='picture_Main_pic',
            field=models.ImageField(null=True, upload_to='instagram/'),
        ),
        migrations.AddField(
            model_name='picture',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
