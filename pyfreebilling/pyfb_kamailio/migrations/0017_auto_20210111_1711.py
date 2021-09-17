# Generated by Django 2.2.17 on 2021-01-11 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyfb_kamailio', '0016_auto_20200527_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acccdr',
            name='o_c_rate_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='originator customer rate Id'),
        ),
        migrations.AlterField(
            model_name='acccdr',
            name='o_c_rate_type',
            field=models.IntegerField(blank=True, null=True, verbose_name='originator customer rate type'),
        ),
        migrations.AlterField(
            model_name='acccdr',
            name='o_p_rate_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='originator provider rate Id'),
        ),
        migrations.AlterField(
            model_name='acccdr',
            name='o_p_rate_type',
            field=models.IntegerField(blank=True, null=True, verbose_name='originator provider rate type'),
        ),
        migrations.AlterField(
            model_name='acccdr',
            name='orig_customer',
            field=models.IntegerField(blank=True, null=True, verbose_name='originator customer'),
        ),
        migrations.AlterField(
            model_name='acccdr',
            name='orig_provider',
            field=models.IntegerField(blank=True, null=True, verbose_name='originator provider'),
        ),
        migrations.AlterField(
            model_name='acccdr',
            name='t_c_rate_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='terminator customer rate Id'),
        ),
        migrations.AlterField(
            model_name='acccdr',
            name='t_c_rate_type',
            field=models.IntegerField(blank=True, null=True, verbose_name='terminator customer rate type'),
        ),
        migrations.AlterField(
            model_name='acccdr',
            name='t_p_rate_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='terminator provider rate Id'),
        ),
        migrations.AlterField(
            model_name='acccdr',
            name='t_p_rate_type',
            field=models.IntegerField(blank=True, null=True, verbose_name='terminator provider rate type'),
        ),
        migrations.AlterField(
            model_name='acccdr',
            name='term_customer',
            field=models.IntegerField(blank=True, null=True, verbose_name='terminator customer'),
        ),
        migrations.AlterField(
            model_name='acccdr',
            name='term_provider',
            field=models.IntegerField(blank=True, null=True, verbose_name='terminator provider'),
        ),
    ]