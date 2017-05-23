# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-25 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyfreebill', '0002_auto_20161012_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cdr',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='cdr',
            name='gateway',
        ),
        migrations.RemoveField(
            model_name='cdr',
            name='lcr_carrier_id',
        ),
        migrations.RemoveField(
            model_name='cdr',
            name='lcr_group_id',
        ),
        migrations.RemoveField(
            model_name='cdr',
            name='ratecard_id',
        ),
        migrations.AlterField(
            model_name='company',
            name='email_alert',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='alert email address'),
        ),
        migrations.AlterField(
            model_name='emailaddress',
            name='email_address',
            field=models.EmailField(max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='group',
            name='companies',
            field=models.ManyToManyField(blank=True, to='pyfreebill.Company', verbose_name='companies'),
        ),
        migrations.AlterField(
            model_name='group',
            name='people',
            field=models.ManyToManyField(blank=True, to='pyfreebill.Person', verbose_name='people'),
        ),
        migrations.DeleteModel(
            name='CDR',
        ),
    ]