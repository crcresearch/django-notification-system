# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-06 15:06
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20181105_0902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='content',
        ),
        migrations.RemoveField(
            model_name='optout',
            name='end',
        ),
        migrations.RemoveField(
            model_name='optout',
            name='start',
        ),
        migrations.AddField(
            model_name='notification',
            name='body',
            field=models.TextField(default='body'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='extra',
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True, default={}, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='title',
            field=models.CharField(default='title', max_length=50),
            preserve_default=False,
        ),
        # migrations.AlterUniqueTogether(
        #     name='notification',
        #     unique_together=set(
        #         [('user_target', 'scheduled_delivery', 'title', 'body')]),
        # ),
        migrations.AlterField(
            model_name='notification',
            name='user_target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='notifications', to='notifications.UserTarget'),
        )
    ]
