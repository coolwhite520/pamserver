# Generated by Django 2.2.10 on 2020-03-17 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpack', '0015_auto_20200311_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syncinstancetask',
            name='date_last_sync',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date last sync'),
        ),
    ]
