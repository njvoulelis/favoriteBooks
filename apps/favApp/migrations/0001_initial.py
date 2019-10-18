# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-17 19:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logRegApp', '0002_auto_20191015_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('uploadedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booksUploaded', to='logRegApp.User')),
                ('usersWhoLike', models.ManyToManyField(related_name='likedBooks', to='logRegApp.User')),
            ],
        ),
    ]