# Generated by Django 2.1.7 on 2019-06-24 13:51

import common.fields.model
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpack', '0008_auto_20190404_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changeauthplan',
            name='password',
            field=common.fields.model.EncryptCharField(blank=True, max_length=256, null=True, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='changeauthplanexecution',
            name='password',
            field=common.fields.model.EncryptCharField(blank=True, max_length=256, null=True, verbose_name='Password'),
        ),
    ]
