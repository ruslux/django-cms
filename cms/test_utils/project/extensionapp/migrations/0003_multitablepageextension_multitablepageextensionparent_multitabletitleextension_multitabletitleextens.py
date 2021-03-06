# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-16 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('extensionapp', '0002_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiTablePageExtensionParent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extension_parent_field', models.CharField(blank=True, default=b'', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MultiTableTitleExtensionParent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extension_title_parent_field', models.CharField(blank=True, default=b'', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MultiTablePageExtension',
            fields=[
                ('multitablepageextensionparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='extensionapp.MultiTablePageExtensionParent')),
                ('multitable_extra', models.CharField(blank=True, default=b'', max_length=255)),
                ('extended_object', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='cms.Page')),
                ('public_extension', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='draft_extension', to='extensionapp.MultiTablePageExtension')),
            ],
            options={
                'abstract': False,
            },
            bases=('extensionapp.multitablepageextensionparent', models.Model),
        ),
        migrations.CreateModel(
            name='MultiTableTitleExtension',
            fields=[
                ('multitabletitleextensionparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='extensionapp.MultiTableTitleExtensionParent')),
                ('multitable_extra_title', models.CharField(blank=True, default=b'', max_length=255)),
                ('extended_object', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='cms.Title')),
                ('public_extension', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='draft_extension', to='extensionapp.MultiTableTitleExtension')),
            ],
            options={
                'abstract': False,
            },
            bases=('extensionapp.multitabletitleextensionparent', models.Model),
        ),
    ]
