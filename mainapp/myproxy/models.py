from django.db import models


# Create your models here.


class Proxy(models.Model):
    resourse = models.CharField('来源', max_length=50)

    ip = models.CharField('IP', max_length=50, blank=True, null=True)
    port = models.CharField('Port', max_length=20, blank=True, null=True)
    head = models.CharField('Head', max_length=10, blank=True, null=True)
    STATUS = (
        ('V', 'VAILD'),
        ('I', 'INVAILD')
    )
    status = models.CharField('状态', max_length=10, choices=STATUS)

    TYPE = (
        ('G', '高匿'),
        ('T', '透明'),
        ('O', '其他')
    )
    type = models.CharField('类型', max_length=10, choices=TYPE, default='O')

    district =models.CharField('地区', max_length=50, default='其他')

    Vaildated = models.IntegerField('通过验证次数', blank=True, null=True, default=1)
    failed_time  = models.IntegerField('未通过验证次数', blank=True, null=True, default=0)

    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now_add=True)

    def __str__(self):
        return self.ip

    class meta:
        ordering = ['-last_modified_time']