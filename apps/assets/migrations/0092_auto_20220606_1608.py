# Generated by Django 3.1.14 on 2022-06-06 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0091_auto_20220602_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminuser',
            name='can_moveout',
        ),
        migrations.RemoveField(
            model_name='authbook',
            name='can_moveout',
        ),
        migrations.RemoveField(
            model_name='gateway',
            name='can_moveout',
        ),
        migrations.RemoveField(
            model_name='historicalauthbook',
            name='can_moveout',
        ),
        migrations.RemoveField(
            model_name='systemuser',
            name='can_moveout',
        ),
    ]
