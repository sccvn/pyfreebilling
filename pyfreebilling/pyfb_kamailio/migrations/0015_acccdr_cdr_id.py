# Generated by Django 2.1.5 on 2020-05-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyfb_kamailio', '0014_auto_20200518_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='acccdr',
            name='cdr_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='CDR Id'),
        ),
    ]