# Generated by Django 3.1.6 on 2021-08-27 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpack', '0034_auto_20210810_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='provider',
            field=models.CharField(choices=[('aliyun', 'Alibaba Cloud'), ('aws_international', 'AWS (International)'), ('aws_china', 'AWS (China)'), ('azure', 'Azure (China)'), ('azure_international', 'Azure (International)'), ('huaweicloud', 'Huawei Cloud'), ('qcloud', 'Tencent Cloud'), ('vmware', 'VMware'), ('nutanix', 'Nutanix'), ('huaweicloud_private', 'Huawei Private Cloud'), ('qingcloud_private', 'Qingyun Private Cloud'), ('gcp', 'Google Cloud Platform')], default='aliyun', max_length=128, verbose_name='Provider'),
        )
    ]
