# Generated by Django 3.1.14 on 2022-06-02 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0090_auto_20220412_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminuser',
            name='can_moveout',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='authbook',
            name='can_moveout',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='gateway',
            name='can_moveout',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalauthbook',
            name='can_moveout',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='systemuser',
            name='can_moveout',
            field=models.BooleanField(default=True),
        ),
    ]
