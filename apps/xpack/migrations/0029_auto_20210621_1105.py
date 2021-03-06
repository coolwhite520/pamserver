# Generated by Django 3.1 on 2021-06-21 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpack', '0028_auto_20210408_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='provider',
            field=models.CharField(choices=[('aliyun', 'Alibaba Cloud'), ('aws_international', 'AWS (International)'), ('aws_china', 'AWS (China)'), ('azure', 'Azure (China)'), ('azure_international', 'Azure (International)'), ('huaweicloud', 'Huawei Cloud'), ('qcloud', 'Tencent Cloud'), ('vmware', 'VMware'), ('nutanix', 'Nutanix'), ('huaweicloud_private', 'Huawei Private Cloud'), ('qingcloud_private', 'Qingyun Private Cloud')], default='aliyun', max_length=128, verbose_name='Provider'),
        ),
    ]
