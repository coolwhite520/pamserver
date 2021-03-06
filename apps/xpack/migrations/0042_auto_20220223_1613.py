# Generated by Django 3.1.13 on 2022-02-23 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpack', '0041_auto_20220217_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationchangeauthplan',
            name='type',
            field=models.CharField(choices=[('mysql', 'MySQL'), ('oracle', 'Oracle'), ('postgresql', 'PostgreSQL'), ('mariadb', 'MariaDB'), ('sqlserver', 'SQLServer'), ('redis', 'Redis'), ('mongodb', 'MongoDB'), ('chrome', 'Chrome'), ('mysql_workbench', 'MySQL Workbench'), ('vmware_client', 'vSphere Client'), ('custom', 'Custom'), ('k8s', 'Kubernetes')], max_length=16, verbose_name='Type'),
        ),
    ]
