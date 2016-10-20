# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 03:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AuthorID', models.IntegerField()),
                ('Name', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
                ('Country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.IntegerField()),
                ('Title', models.CharField(max_length=100)),
                ('AuthorID', models.IntegerField()),
                ('Publisher', models.CharField(max_length=100)),
                ('PublishDate', models.DateTimeField()),
                ('Price', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tushuguanli.Author')),
            ],
        ),
    ]