# Generated by Django 2.2.2 on 2019-06-16 22:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0004_auto_20190616_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcMstr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8, verbose_name='Code')),
                ('name', models.CharField(max_length=50, verbose_name='Full name')),
                ('address_1', models.CharField(default='-', max_length=50, verbose_name='Address line 1')),
                ('address_2', models.CharField(default='-', max_length=50, verbose_name='Address line 2')),
                ('city', models.CharField(max_length=15, null=True, verbose_name='City')),
                ('pin', models.CharField(default='-', max_length=6, verbose_name='ZIP / Postal code')),
                ('state_code', models.CharField(default='-', max_length=2, verbose_name='State Code')),
                ('gst_no', models.CharField(default='-', max_length=15, verbose_name='GST Number')),
                ('pan_aadhar_no', models.CharField(default='-', max_length=16, verbose_name='PAN / Aadhar Number')),
                ('bp_type', models.CharField(max_length=10, verbose_name='Business Partner Type')),
                ('group_code', models.CharField(blank=True, default='-', max_length=3, verbose_name='Business Group')),
                ('bsgrp', models.IntegerField(default=0, verbose_name='Balance Sheet Group')),
                ('bssubgrp', models.IntegerField(default=0, verbose_name='Balance Sheet Sub-Group')),
                ('opbal', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=14, verbose_name='Opening Balance')),
                ('clbal', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=14, verbose_name='Closing Balance')),
                ('temp_bal', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=14, verbose_name='Temp. Balance')),
                ('user', models.CharField(max_length=20, verbose_name='User')),
                ('upd_time', models.DateTimeField(auto_now=True, verbose_name='Update Date and Time')),
                ('share_dep', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Share-Dep %')),
                ('email', models.CharField(max_length=35, verbose_name='Email')),
                ('phone', models.CharField(max_length=25, verbose_name='Phone')),
                ('pwd', models.CharField(max_length=15, verbose_name='Password')),
            ],
        ),
        migrations.CreateModel(
            name='ItemMstr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('it_code', models.CharField(max_length=8, verbose_name='Item Code')),
                ('it_name', models.CharField(max_length=20, verbose_name='Item Name')),
                ('location', models.CharField(max_length=25, verbose_name='Location')),
                ('sac_code', models.IntegerField(default=998363, verbose_name='SAC Code')),
                ('gst', models.DecimalField(decimal_places=2, default=5, max_digits=2, verbose_name='GST')),
            ],
        ),
        migrations.CreateModel(
            name='ShowMstr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_code', models.CharField(max_length=8, verbose_name='Show Code')),
                ('show_name', models.CharField(max_length=30, verbose_name='Show Name')),
                ('start_date', models.DateField(default=django.utils.datetime_safe.date.today, verbose_name='Start Date')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisement.AcMstr')),
            ],
        ),
    ]
