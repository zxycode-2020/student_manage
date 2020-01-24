# coding:utf8
from django.db import models
# Create your models here.

# banner轮表表
class Slider(models.Model):
    active_choices = ((1, '显示'), (0, '不显示'))
    is_active = models.IntegerField(choices=active_choices, verbose_name='是否上线', default=1)
    name = models.CharField(verbose_name='标识', max_length=30, unique=True)
    link = models.CharField(verbose_name='链接', max_length=256)
    img = models.ImageField(verbose_name='轮播图片', upload_to='./static/images/focus')
    weight = models.IntegerField(verbose_name='权重', default=0)
    date_add = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)

    class Meta:
        ordering = ['-weight']
        verbose_name = verbose_name_plural = '首页轮播'

    def __unicode__(self):
        return self.name


# 公告
class Notice(models.Model):
    active_choices = ((0, '不显示'), (1, '显示'))
    is_active = models.IntegerField(verbose_name='是否显示', choices=active_choices, default=1)
    title = models.CharField(verbose_name='标题', max_length=30)
    description = models.CharField(verbose_name='简介', max_length=500)
    detail = models.TextField(verbose_name='详细内容', null=True, blank=True)
    weight = models.IntegerField(verbose_name='权重', default=0)

    class Meta:
        ordering = ['-weight']
        verbose_name = verbose_name_plural = '公告'

    def __unicode__(self):
        return self.title

# 课程表
class Course(models.Model):
    status_choice = (
        (0, u'下线'),
        (1, u'上线'),
    )
    status = models.IntegerField(verbose_name='状态', choices=status_choice, default=1)
    weight = models.IntegerField(verbose_name='权重', default=0)
    icon = models.ImageField(verbose_name='图标', upload_to='./static/images/icon/', null=True, blank=True)
    name = models.CharField(verbose_name='名称', max_length=32, db_index=True, unique=True)
    summary = models.CharField(verbose_name='简介', max_length=40, default='summary')

    class Meta:
        db_table = 'Course'
        verbose_name_plural = u'课程'

    def __unicode__(self):
        return self.name

# 学员表
class Student(models.Model):
    status_choice = (
        (0, u'下线'),
        (1, u'上线'),
    )
    status = models.IntegerField(verbose_name='状态', choices=status_choice, default=1)
    weight = models.IntegerField(verbose_name='权重（按从大到小排列）', default=0)
    pic = models.ImageField(verbose_name='学员头像', upload_to='./static/images/student_pic/', null=True, blank=True)
    name = models.CharField(verbose_name='名称', max_length=32, db_index=True, unique=True)
    company = models.CharField(verbose_name='就业单位', max_length=32)
    salary = models.CharField(verbose_name='薪水', max_length=32)

    class Meta:
        db_table = 'Student'
        verbose_name_plural = u'学生信息'

    def __unicode__(self):
        return self.name

# 学员详细表
class StudentDetail(models.Model):
    student = models.OneToOneField('Student')
    weight = models.IntegerField(verbose_name='权重（按从大到小排列）', default=0)
    letter_of_thanks = models.CharField(verbose_name='学员感谢信', max_length=256)

    class Meta:
        db_table = 'StudentDetail'
        verbose_name_plural = u'学生更多信息'

    def __unicode__(self):
        return self.student.name

# 招聘信息表
class Recruit(models.Model):
    status_choice = (
        (0, u'已过期'),
        (1, u'招聘中'),
    )
    status = models.IntegerField(verbose_name='状态', choices=status_choice, default=1)
    weight = models.IntegerField(verbose_name='权重（按从大到小排列）', default=0)
    title = models.CharField(max_length=20)
    salary = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    detail = models.TextField()
    deadline = models.DateField()

    class Meta:
        db_table = 'Recruit'
        verbose_name_plural = u'招聘信息'

    def __unicode__(self):
        return self.title


class Cooperation(models.Model):
    weight = models.IntegerField(verbose_name='权重（按从大到小排列）', default=0)
    href = models.CharField(verbose_name='企业连接', max_length=20, default='javascript:void(0)')
    logo = models.ImageField(verbose_name='企业LOGO', upload_to='./static/images/cooperation/')
    company = models.CharField(verbose_name='公司名称', max_length=20)

    class Meta:
        db_table = 'Cooperation'
        verbose_name_plural = u'企业合作'

    def __unicode__(self):
        return self.company


class Direction(models.Model):
    weight = models.IntegerField(verbose_name='权重（按从大到小排列）', default=0)
    name = models.CharField(verbose_name='名称', max_length=32)
    classification = models.ManyToManyField('Classification')

    class Meta:
        db_table = 'Direction'
        verbose_name_plural = u'方向（视频方向）'

    def __unicode__(self):
        return self.name

# 视频分类表
class Classification(models.Model):
    weight = models.IntegerField(verbose_name='权重（按从大到小排列）', default=0)
    name = models.CharField(verbose_name='名称', max_length=32)

    class Meta:
        db_table = 'Classification'
        verbose_name_plural = u'分类（视频分类）'

    def __unicode__(self):
        return self.name

# 视频
class Video(models.Model):
    status_choice = (
        (0, u'下线'),
        (1, u'上线'),
    )
    level_choice = (
        (1, u'初级'),
        (2, u'中级'),
        (3, u'高级'),
    )
    status = models.IntegerField(verbose_name='状态', choices=status_choice, default=1)
    level = models.IntegerField(verbose_name='级别', choices=level_choice, default=1)
    classification = models.ForeignKey('Classification', null=True, blank=True)
    weight = models.IntegerField(verbose_name='权重（按从大到小排列）', default=0)
    title = models.CharField(verbose_name='标题', max_length=32)
    summary = models.CharField(verbose_name='简介', max_length=32)
    img = models.ImageField(verbose_name='图片', upload_to='./static/images/Video/')
    href = models.CharField(verbose_name='视频地址', max_length=256)

    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Video'
        verbose_name_plural = u'视频'

    def __unicode__(self):
        return self.title
