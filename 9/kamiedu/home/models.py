#coding:utf8
from django.db import models

# Create your models here.

#首页轮播表
class Banner(models.Model):
    status_choice = [(0,'下线'),(1,'上线')]
    status = models.IntegerField(choices=status_choice,verbose_name='状态',default=1)
    name = models.CharField(verbose_name='名称',max_length=30)
    weight = models.IntegerField(verbose_name='权重：从大到小',default=0)
    img = models.ImageField(verbose_name='banner图片',upload_to='banner/')
    href = models.CharField(verbose_name='图片链接',max_length=300)
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = '首页Banner'

    def __unicode__(self):
        return self.name

#公告
class Notice(models.Model):
    status_choice = [(0,'下线'),(1,'上线')]
    status = models.IntegerField(choices=status_choice,verbose_name='公告是否上线',default=1)
    weight = models.IntegerField(verbose_name='权重：从大到小', default=0)
    title = models.CharField(verbose_name='公告标题',max_length=50)
    description = models.CharField(verbose_name='公告简介',max_length=100)
    content = models.TextField(verbose_name='公告内容')

    class Meta:
        verbose_name_plural = verbose_name = '企业公告'

    def __unicode__(self):
        return self.title

# 课程介绍表
class Course(models.Model):
    status_choice = [(0,'下线'),(1,'上线')]
    status = models.IntegerField(choices=status_choice,verbose_name='课程是否上线',default=1)
    weight = models.IntegerField(verbose_name='权重：从大到小', default=0)
    name = models.CharField(verbose_name='课程名称',max_length='30')
    description = models.CharField(verbose_name='课程简介',max_length=200)
    img = models.ImageField(verbose_name='课程封面',upload_to='course/')

    class Meta:
        verbose_name_plural = verbose_name = '课程介绍表'

    def __unicode__(self):
        return self.name

#学生表
class Student(models.Model):
    status_choice = [(0,'不展示'),(1,'展示')]
    status = models.IntegerField(choices=status_choice,verbose_name='学生是否展示',default=1)
    weight = models.IntegerField(verbose_name='权重：从大到小', default=0)
    name = models.CharField(verbose_name='姓名',max_length=20)
    avatar = models.ImageField(verbose_name='照片',upload_to='avatar/')
    company = models.CharField(verbose_name='就业公司',max_length=100)
    salary = models.CharField(verbose_name='就业薪资',max_length=30)

    class Meta:
        verbose_name_plural = verbose_name = '学生表'

    def __unicode__(self):
        return self.name

#学生详情表
class StuDetail(models.Model):
    student = models.OneToOneField('Student')
    weight = models.IntegerField(verbose_name='权重,从大到小',default=0)
    letter = models.TextField(verbose_name='感谢信')

    class Meta:
        verbose_name_plural = verbose_name = '学生详情表'

    def __unicode__(self):
        return self.student.name

# 招聘信息表
class Recruit(models.Model):
    status_choice = [(0,'下线'),(1,'上线')]
    status = models.IntegerField(choices=status_choice,verbose_name='招聘是否上线',default=1)
    weight = models.IntegerField(verbose_name='权重：从大到小', default=0)

    title = models.CharField(verbose_name='标题',max_length=100)
    company = models.CharField(verbose_name='公司',max_length=200)
    salary = models.CharField(verbose_name='薪水',max_length=30)
    content = models.TextField(verbose_name='详情')
    date_dead = models.DateTimeField()

    class Meta:
        verbose_name_plural = verbose_name = '招聘信息'

    def __unicode__(self):
        return self.title

# 合作企业表
class Cooperation(models.Model):
    name = models.CharField(verbose_name='公司名称',max_length='100')
    weight = models.IntegerField(default=0,verbose_name='权重从打到小')
    logo = models.ImageField(verbose_name='企业logo',upload_to='logos/')
    link = models.CharField(verbose_name='链接地址',max_length='300')

    class Meta:
        verbose_name_plural = verbose_name = '合作企业'

    def __unicode__(self):
        return self.name

# 建立老师表




