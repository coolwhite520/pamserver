# Generated by Django 3.1.14 on 2022-03-10 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpack', '0042_auto_20220223_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'permissions': [('test_account', 'Test cloud account')], 'verbose_name': 'Cloud account'},
        ),
    ]