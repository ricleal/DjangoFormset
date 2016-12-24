# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 18:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', related_query_name='book', to='app2.Author'),
        ),
    ]