# Generated by Django 2.1.4 on 2018-12-20 10:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields
import model_utils.fields
import partial_index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pyfb_endpoint', '0004_auto_20181219_1402'),
        ('pyfb_rating', '0002_auto_20181207_1517'),
        ('pyfb_direction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', models.CharField(choices=[('enabled', 'Enabled'), ('disabled', 'Disabled'), ('blocked', 'Blocked')], default='enabled', help_text='State of the rate : enabled / blocked - calls to this destination are blocked / disabled', max_length=20, verbose_name='Status')),
                ('route_type', models.CharField(choices=[('LCR', 'Least cost'), ('PRIO', 'Priority'), ('WEIGHT', 'Weight'), ('QUALITY', 'Quality')], default='LCR', max_length=10, verbose_name='route type')),
                ('weight', models.PositiveIntegerField(default=1)),
                ('priority', models.PositiveIntegerField(default=1)),
            ],
            options={
                'ordering': ('country',),
                'db_table': 'pyfb_routing_countryrule',
            },
        ),
        migrations.CreateModel(
            name='CountryTypeRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', models.CharField(choices=[('enabled', 'Enabled'), ('disabled', 'Disabled'), ('blocked', 'Blocked')], default='enabled', help_text='State of the rate : enabled / blocked - calls to this destination are blocked / disabled', max_length=20, verbose_name='Status')),
                ('route_type', models.CharField(choices=[('LCR', 'Least cost'), ('PRIO', 'Priority'), ('WEIGHT', 'Weight'), ('QUALITY', 'Quality')], default='LCR', max_length=10, verbose_name='route type')),
                ('weight', models.PositiveIntegerField(default=1)),
                ('priority', models.PositiveIntegerField(default=1)),
            ],
            options={
                'ordering': ('country', 'type'),
                'db_table': 'pyfb_routing_countrytype_rule',
            },
        ),
        migrations.CreateModel(
            name='DefaultRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', models.CharField(choices=[('enabled', 'Enabled'), ('disabled', 'Disabled'), ('blocked', 'Blocked')], default='enabled', help_text='State of the rate : enabled / blocked - calls to this destination are blocked / disabled', max_length=20, verbose_name='Status')),
                ('route_type', models.CharField(choices=[('LCR', 'Least cost'), ('PRIO', 'Priority'), ('WEIGHT', 'Weight'), ('QUALITY', 'Quality')], default='LCR', max_length=10, verbose_name='route type')),
                ('weight', models.PositiveIntegerField(default=1)),
                ('priority', models.PositiveIntegerField(default=1)),
            ],
            options={
                'ordering': ('-pk',),
                'db_table': 'pyfb_routing_default_rule',
            },
        ),
        migrations.CreateModel(
            name='DestinationRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', models.CharField(choices=[('enabled', 'Enabled'), ('disabled', 'Disabled'), ('blocked', 'Blocked')], default='enabled', help_text='State of the rate : enabled / blocked - calls to this destination are blocked / disabled', max_length=20, verbose_name='Status')),
                ('route_type', models.CharField(choices=[('LCR', 'Least cost'), ('PRIO', 'Priority'), ('WEIGHT', 'Weight'), ('QUALITY', 'Quality')], default='LCR', max_length=10, verbose_name='route type')),
                ('weight', models.PositiveIntegerField(default=1)),
                ('priority', models.PositiveIntegerField(default=1)),
            ],
            options={
                'ordering': ('destination',),
                'db_table': 'pyfb_routing_destination_rule',
            },
        ),
        migrations.CreateModel(
            name='PrefixRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', models.CharField(choices=[('enabled', 'Enabled'), ('disabled', 'Disabled'), ('blocked', 'Blocked')], default='enabled', help_text='State of the rate : enabled / blocked - calls to this destination are blocked / disabled', max_length=20, verbose_name='Status')),
                ('route_type', models.CharField(choices=[('LCR', 'Least cost'), ('PRIO', 'Priority'), ('WEIGHT', 'Weight'), ('QUALITY', 'Quality')], default='LCR', max_length=10, verbose_name='route type')),
                ('weight', models.PositiveIntegerField(default=1)),
                ('priority', models.PositiveIntegerField(default=1)),
                ('prefix', models.CharField(db_index=True, max_length=30, verbose_name='numeric prefix')),
                ('destnum_length', models.PositiveSmallIntegerField(default=0, help_text='If value > 0, then destination number must match tsi length', verbose_name='Destination number length')),
            ],
            options={
                'ordering': ('prefix', '-destnum_length'),
                'db_table': 'pyfb_routing_prefix_rule',
            },
        ),
        migrations.CreateModel(
            name='RegionRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', models.CharField(choices=[('enabled', 'Enabled'), ('disabled', 'Disabled'), ('blocked', 'Blocked')], default='enabled', help_text='State of the rate : enabled / blocked - calls to this destination are blocked / disabled', max_length=20, verbose_name='Status')),
                ('route_type', models.CharField(choices=[('LCR', 'Least cost'), ('PRIO', 'Priority'), ('WEIGHT', 'Weight'), ('QUALITY', 'Quality')], default='LCR', max_length=10, verbose_name='route type')),
                ('weight', models.PositiveIntegerField(default=1)),
                ('priority', models.PositiveIntegerField(default=1)),
            ],
            options={
                'ordering': ('region',),
                'db_table': 'pyfb_routing_region_rule',
            },
        ),
        migrations.CreateModel(
            name='RegionTypeRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', models.CharField(choices=[('enabled', 'Enabled'), ('disabled', 'Disabled'), ('blocked', 'Blocked')], default='enabled', help_text='State of the rate : enabled / blocked - calls to this destination are blocked / disabled', max_length=20, verbose_name='Status')),
                ('route_type', models.CharField(choices=[('LCR', 'Least cost'), ('PRIO', 'Priority'), ('WEIGHT', 'Weight'), ('QUALITY', 'Quality')], default='LCR', max_length=10, verbose_name='route type')),
                ('weight', models.PositiveIntegerField(default=1)),
                ('priority', models.PositiveIntegerField(default=1)),
            ],
            options={
                'ordering': ('region', 'type'),
                'db_table': 'pyfb_routing_regiontype_rule',
            },
        ),
        migrations.CreateModel(
            name='RoutingGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[('enabled', 'Enabled'), ('disabled', 'Disabled')], default='enabled', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'ordering': ('name',),
                'db_table': 'pyfb_routing_routinggroup',
            },
        ),
        migrations.AddField(
            model_name='regiontyperule',
            name='c_route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfb_routing.RoutingGroup'),
        ),
        migrations.AddField(
            model_name='regiontyperule',
            name='provider_gateway_list',
            field=models.ManyToManyField(to='pyfb_endpoint.ProviderEndpoint'),
        ),
        migrations.AddField(
            model_name='regiontyperule',
            name='provider_ratecard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pyfb_rating.ProviderRatecard'),
        ),
        migrations.AddField(
            model_name='regiontyperule',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfb_direction.Region'),
        ),
        migrations.AddField(
            model_name='regiontyperule',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfb_direction.Type'),
        ),
        migrations.AddField(
            model_name='regionrule',
            name='c_route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfb_routing.RoutingGroup'),
        ),
        migrations.AddField(
            model_name='regionrule',
            name='provider_gateway_list',
            field=models.ManyToManyField(to='pyfb_endpoint.ProviderEndpoint'),
        ),
        migrations.AddField(
            model_name='regionrule',
            name='provider_ratecard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pyfb_rating.ProviderRatecard'),
        ),
        migrations.AddField(
            model_name='regionrule',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfb_direction.Region'),
        ),
        migrations.AddField(
            model_name='prefixrule',
            name='c_route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfb_routing.RoutingGroup'),
        ),
        migrations.AddField(
            model_name='prefixrule',
            name='provider_gateway_list',
            field=models.ManyToManyField(to='pyfb_endpoint.ProviderEndpoint'),
        ),
        migrations.AddField(
            model_name='prefixrule',
            name='provider_ratecard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pyfb_rating.ProviderRatecard'),
        ),
        migrations.AddField(
            model_name='destinationrule',
            name='c_route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfb_routing.RoutingGroup'),
        ),
        migrations.AddField(
            model_name='destinationrule',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfb_direction.Destination'),
        ),
        migrations.AddField(
            model_name='destinationrule',
            name='provider_gateway_list',
            field=models.ManyToManyField(to='pyfb_endpoint.ProviderEndpoint'),
        ),
        migrations.AddField(
            model_name='destinationrule',
            name='provider_ratecard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pyfb_rating.ProviderRatecard'),
        ),
        migrations.AddField(
            model_name='defaultrule',
            name='c_route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfb_routing.RoutingGroup'),
        ),
        migrations.AddField(
            model_name='defaultrule',
            name='provider_gateway_list',
            field=models.ManyToManyField(to='pyfb_endpoint.ProviderEndpoint'),
        ),
        migrations.AddField(
            model_name='defaultrule',
            name='provider_ratecard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pyfb_rating.ProviderRatecard'),
        ),
        migrations.AddField(
            model_name='countrytyperule',
            name='c_route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfb_routing.RoutingGroup'),
        ),
        migrations.AddField(
            model_name='countrytyperule',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfb_direction.Country'),
        ),
        migrations.AddField(
            model_name='countrytyperule',
            name='provider_gateway_list',
            field=models.ManyToManyField(to='pyfb_endpoint.ProviderEndpoint'),
        ),
        migrations.AddField(
            model_name='countrytyperule',
            name='provider_ratecard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pyfb_rating.ProviderRatecard'),
        ),
        migrations.AddField(
            model_name='countrytyperule',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfb_direction.Type'),
        ),
        migrations.AddField(
            model_name='countryrule',
            name='c_route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfb_routing.RoutingGroup'),
        ),
        migrations.AddField(
            model_name='countryrule',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfb_direction.Country'),
        ),
        migrations.AddField(
            model_name='countryrule',
            name='provider_gateway_list',
            field=models.ManyToManyField(to='pyfb_endpoint.ProviderEndpoint'),
        ),
        migrations.AddField(
            model_name='countryrule',
            name='provider_ratecard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pyfb_rating.ProviderRatecard'),
        ),
        migrations.AddIndex(
            model_name='regiontyperule',
            index=partial_index.PartialIndex(fields=['c_route', 'region', 'type', 'provider_ratecard'], name='pyfb_routin_c_route_640542_partial', unique=True, where="status <> 'disabled'"),
        ),
        migrations.AlterUniqueTogether(
            name='regiontyperule',
            unique_together={('c_route', 'region', 'type', 'provider_ratecard')},
        ),
        migrations.AddIndex(
            model_name='regionrule',
            index=partial_index.PartialIndex(fields=['c_route', 'region', 'provider_ratecard'], name='pyfb_routin_c_route_a1def0_partial', unique=True, where="status <> 'disabled'"),
        ),
        migrations.AlterUniqueTogether(
            name='regionrule',
            unique_together={('c_route', 'region', 'provider_ratecard')},
        ),
        migrations.AddIndex(
            model_name='prefixrule',
            index=partial_index.PartialIndex(fields=['c_route', 'prefix', 'destnum_length', 'provider_ratecard'], name='pyfb_routin_c_route_05cda0_partial', unique=True, where="status <> 'disabled'"),
        ),
        migrations.AlterUniqueTogether(
            name='prefixrule',
            unique_together={('c_route', 'prefix', 'destnum_length', 'provider_ratecard')},
        ),
        migrations.AddIndex(
            model_name='destinationrule',
            index=partial_index.PartialIndex(fields=['c_route', 'destination', 'provider_ratecard'], name='pyfb_routin_c_route_beaed1_partial', unique=True, where="status <> 'disabled'"),
        ),
        migrations.AlterUniqueTogether(
            name='destinationrule',
            unique_together={('c_route', 'destination', 'provider_ratecard')},
        ),
        migrations.AddIndex(
            model_name='defaultrule',
            index=partial_index.PartialIndex(fields=['c_route', 'provider_ratecard'], name='pyfb_routin_c_route_804b88_partial', unique=True, where="status <> 'disabled'"),
        ),
        migrations.AlterUniqueTogether(
            name='defaultrule',
            unique_together={('c_route', 'provider_ratecard')},
        ),
        migrations.AddIndex(
            model_name='countrytyperule',
            index=partial_index.PartialIndex(fields=['c_route', 'country', 'type', 'provider_ratecard'], name='pyfb_routin_c_route_d477b5_partial', unique=True, where="status <> 'disabled'"),
        ),
        migrations.AlterUniqueTogether(
            name='countrytyperule',
            unique_together={('c_route', 'country', 'type', 'provider_ratecard')},
        ),
        migrations.AddIndex(
            model_name='countryrule',
            index=partial_index.PartialIndex(fields=['c_route', 'country', 'provider_ratecard'], name='pyfb_routin_c_route_676371_partial', unique=True, where="status <> 'disabled'"),
        ),
        migrations.AlterUniqueTogether(
            name='countryrule',
            unique_together={('c_route', 'country', 'provider_ratecard')},
        ),
    ]