# Generated by Django 2.2.10 on 2020-04-07 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpack', '0017_auto_20200324_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='syncinstancetask',
            name='covered_always',
            field=models.BooleanField(default=False, verbose_name='Covered always'),
        ),
    ]
