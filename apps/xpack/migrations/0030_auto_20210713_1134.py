# Generated by Django 3.1.6 on 2021-07-13 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0076_delete_assetuser'),
        ('xpack', '0029_auto_20210621_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syncinstancetask',
            name='admin_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.systemuser', verbose_name='Admin user'),
        ),
    ]
