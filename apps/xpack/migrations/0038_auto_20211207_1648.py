# Generated by Django 3.1.13 on 2021-12-07 08:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('xpack', '0037_auto_20211026_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationchangeauthplan',
            name='recipients',
            field=models.ManyToManyField(blank=True, related_name='recipient_application_change_auth_plans', to=settings.AUTH_USER_MODEL, verbose_name='Recipient'),
        ),
        migrations.AddField(
            model_name='changeauthplan',
            name='recipients',
            field=models.ManyToManyField(blank=True, related_name='recipient_change_auth_plans', to=settings.AUTH_USER_MODEL, verbose_name='Recipient'),
        ),
        migrations.AlterField(
            model_name='account',
            name='provider',
            field=models.CharField(choices=[('aliyun', 'Alibaba Cloud'), ('aws_international', 'AWS (International)'), ('aws_china', 'AWS (China)'), ('azure', 'Azure (China)'), ('azure_international', 'Azure (International)'), ('huaweicloud', 'Huawei Cloud'), ('qcloud', 'Tencent Cloud'), ('vmware', 'VMware'), ('nutanix', 'Nutanix'), ('huaweicloud_private', 'Huawei Private Cloud'), ('qingcloud_private', 'Qingyun Private Cloud'), ('openstack', 'OpenStack'), ('gcp', 'Google Cloud Platform')], default='aliyun', max_length=128, verbose_name='Provider'),
        ),
        migrations.AlterField(
            model_name='applicationchangeauthplan',
            name='type',
            field=models.CharField(choices=[('mysql', 'MySQL'), ('oracle', 'Oracle'), ('postgresql', 'PostgreSQL'), ('mariadb', 'MariaDB'), ('sqlserver', 'SQLServer'), ('chrome', 'Chrome'), ('mysql_workbench', 'MySQL Workbench'), ('vmware_client', 'vSphere Client'), ('custom', 'Custom'), ('k8s', 'Kubernetes')], max_length=16, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='applicationchangeauthplantask',
            name='is_success',
            field=models.BooleanField(default=False, verbose_name='Is success'),
        ),
        migrations.AlterField(
            model_name='changeauthplantask',
            name='is_success',
            field=models.BooleanField(default=False, verbose_name='Is success'),
        ),
    ]
