# Generated by Django 3.1.13 on 2021-10-26 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0012_auto_20211014_2209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'ordering': ('name',), 'verbose_name': 'Application'},
        ),
    ]
