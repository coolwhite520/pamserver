# Generated by Django 2.1.7 on 2019-04-02 08:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpack', '0006_auto_20190325_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changeauthplan',
            name='assets',
            field=models.ManyToManyField(blank=True, related_name='change_auth_plan', to='assets.Asset', verbose_name='Assets'),
        ),
        migrations.AlterField(
            model_name='changeauthplan',
            name='username',
            field=models.CharField(max_length=32, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z_@\\-\\.]*$', 'Special char not allowed')], verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='changeauthplanexecutionsubtask',
            name='username',
            field=models.CharField(max_length=32, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z_@\\-\\.]*$', 'Special char not allowed')], verbose_name='Username'),
        ),
    ]
