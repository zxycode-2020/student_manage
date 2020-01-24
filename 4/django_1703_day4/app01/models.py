#coding:utf8
from django.db import models

# Create your models here.

class Student(models.Model):
    # 主键id  自动生成一个字段，自增，主键
    # null=True 数据库中可以为空
    # blank=True django自带后台允许为空
    name = models.CharField(verbose_name='学生姓名',max_length=30) # maxlength 最大长度
    age = models.IntegerField(verbose_name='学生年龄',default=18) # default 默认值
    score = models.DecimalField(verbose_name='学生成绩',max_digits=5,decimal_places=2,null=True,blank=True) # 最大位数和小数位多少
    email = models.EmailField(verbose_name='学生邮箱',max_length=100,null=True,blank=True) # varchar  django自带后台验证功能
    ip = models.GenericIPAddressField(max_length=50,null=True,blank=True)
    date_add = models.DateTimeField(auto_now_add=True)
    cls = models.ForeignKey('Class',default=1)

    # 给学生一个实例（对象）起别名 python2 写法
    def __unicode__(self):
        return self.name

    # python3 写法
    def __str__(self):
        return self.name

    # 给表配置一些信息
    class Meta:
        verbose_name = verbose_name_plural = '学生表'

# 班级表
class Class(models.Model):
    name = models.CharField(verbose_name='班级名',max_length=20) # 班级名称

    class Meta:
        verbose_name = verbose_name_plural = '班级表'

    def __unicode__(self):
        return self.name