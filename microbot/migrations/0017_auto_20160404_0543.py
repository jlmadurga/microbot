# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microbot', '0016_auto_20160404_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handler',
            name='source_states',
            field=models.ManyToManyField(blank=True, help_text='Bot states the Handler executes. Set none if any.', related_name='source_handlers', to='microbot.State', verbose_name='Source States'),
        ),
    ]