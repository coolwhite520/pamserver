# Generated by Django 2.2.10 on 2020-03-23 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpack', '0016_auto_20200317_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changeauthplantask',
            name='step',
            field=models.SmallIntegerField(choices=[(0, 'Ready'), (1, 'Preflight check'), (2, 'Change auth'), (3, 'Verify auth'), (4, 'Keep auth'), (10, 'Finished')], default=0, verbose_name='Step'),
        ),
    ]