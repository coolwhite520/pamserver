# Generated by Django 2.1.7 on 2019-07-29 08:03

import common.fields.model
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpack', '0009_auto_20190624_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='_access_key_id',
            new_name='access_key_id',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='_access_key_secret',
            new_name='access_key_secret',
        ),
        migrations.AlterField(
            model_name='account',
            name='access_key_id',
            field=common.fields.model.EncryptCharField(blank=True, max_length=128, null=True, verbose_name='Access key id'),
        ),
        migrations.AlterField(
            model_name='account',
            name='access_key_secret',
            field=common.fields.model.EncryptCharField(blank=True, max_length=128, null=True, verbose_name='Access key secret'),
        ),
        migrations.AddField(
            model_name='syncinstancetask',
            name='crontab',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Regularly perform'),
        ),
        migrations.AddField(
            model_name='syncinstancetask',
            name='interval',
            field=models.IntegerField(blank=True, default=24, null=True, validators=[django.core.validators.MaxValueValidator(8760), django.core.validators.MinValueValidator(1)], verbose_name='Cycle perform'),
        ),
        migrations.AddField(
            model_name='syncinstancetask',
            name='is_periodic',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='syncinstancetask',
            name='instances',
            field=common.fields.model.JsonListCharField(blank=True, max_length=1024, null=True, verbose_name='Instances'),
        ),
        migrations.AlterField(
            model_name='syncinstancetask',
            name='regions',
            field=common.fields.model.JsonListCharField(blank=True, max_length=1024, null=True, verbose_name='Regions'),
        ),
    ]