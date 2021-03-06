# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-27 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('civictechprojects', '0028_auto_20190722_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCommit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_link', models.CharField(max_length=2083)),
                ('user_avatar_link', models.CharField(max_length=2083)),
                ('commit_date', models.DateTimeField()),
                ('commit_sha', models.CharField(max_length=40)),
                ('commit_title', models.CharField(max_length=2000)),
                ('branch_name', models.CharField(max_length=200)),
                ('repo_name', models.CharField(max_length=200)),
                ('commit_project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commits', to='civictechprojects.Project')),
            ],
        ),
    ]
