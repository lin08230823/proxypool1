# Generated by Django 2.0.1 on 2018-04-27 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proxy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.CharField(max_length=50, verbose_name='来源')),
                ('ip', models.CharField(blank=True, max_length=50, null=True, verbose_name='IP')),
                ('port', models.CharField(blank=True, max_length=20, null=True, verbose_name='Port')),
                ('head', models.CharField(blank=True, max_length=10, null=True, verbose_name='Head')),
                ('status', models.CharField(choices=[('V', 'VAILD'), ('I', 'INVAILD')], max_length=10, verbose_name='状态')),
                ('type', models.CharField(choices=[('G', '高匿'), ('T', '透明'), ('O', '其他')], default='O', max_length=10, verbose_name='类型')),
                ('district', models.CharField(default='其他', max_length=50, verbose_name='地区')),
                ('Vaildated', models.IntegerField(blank=True, default=1, null=True, verbose_name='通过验证次数')),
                ('failed_time', models.IntegerField(blank=True, default=0, null=True, verbose_name='未通过验证次数')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
            ],
        ),
    ]
