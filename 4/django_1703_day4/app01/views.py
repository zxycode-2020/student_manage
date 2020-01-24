#coding:utf8
from django.shortcuts import render,HttpResponse
from django.db.models import Count,Avg,Sum

# Create your views here.
import models

def add(request):
    # object 模型管理器
    # 增加 方法1
    # s1 = models.Student()
    # s1.name = '小美'
    # s1.age = 8
    # s1.score = 100.11
    # s1.email = '1@2.com'
    # s1.save()
    # print s1,type(s1)

    # 增加方法2
    # s1 = models.Student(name='小妹',age='16',score='88.88')
    # s1.save()

    # 增加方法 3
    # models.Student.objects.create(name='小媚',age='17',score='77.77')

    # 增加方法 4
    stu_info = {
        'name' : u'XIAOMEI',
        'age' : 15,
        'score' : 66.66,
    }
    models.Student.objects.create(**stu_info)

    return HttpResponse('ok')

# 删除
def delete(request):
    # filter 过滤器，相当于where条件
    res = models.Student.objects.filter(pk=14).delete()
    print res
    return HttpResponse('ok')

# 更新
def update(request):
    # 返回值：影响记录条数
    res = models.Student.objects.filter(pk=1).update(score=300,age=16)
    print res
    return HttpResponse('ok')

# 查询
def select(request):
    # select * from student
    # query 获取查询语句
    # stus = models.Student.objects.all()

    # s1 = models.Student.objects.get(pk=19)
    # print s1

    # gt 大于
    # lt 小于

    #stus = models.Student.objects.filter(id=20)
    #stus = models.Student.objects.filter(name__exact='xiaomei',score__gt=100)
    #stus = models.Student.objects.filter(id__gt=10)[0:3]
    # stus = models.Student.objects.all()
    # stus = list(stus) #转成列表
    # stus1 = stus[:3] # 获取前三条

    # # 获取后三条
    # stus.reverse()
    # stus2 = stus[:3]
    #
    # print stus1
    # print stus2

    # 模糊查询
    #stus = models.Student.objects.filter(name__icontains='xiao') 忽略大小写
    # stus = models.Student.objects.filter(name__contains='xiao') # 不忽略大小写
    # print stus.query
    # print stus

    # 正则表达式查询
    # stus = models.Student.objects.filter(name__regex='^X').all()
    # print stus

    # stus = models.Student.objects.filter(name__iregex='梅$').all()
    # print stus,type(stus)

    # 按照某个字段倒序排列  加 “-”
    # stus = models.Student.objects.all().order_by('-id')
    # stus = models.Student.objects.all().order_by('-age','-score')
    # for stu in stus:
    #     print stu.id,stu.name,stu.age,stu.score

    # 去重复
    # stus = models.Student.objects.all().values('name','age')
    # print stus
    # for stu in stus:
    #     print stu['name'],stu['age']

    # stus = models.Student.objects.all().values_list('name','age') # [('xiaomei',20),(),()]
    # print stus
    # for stu in stus:
    #     print stu[0],stu[1]

    # 去重
    # stus = models.Student.objects.all().values('name','score').distinct()
    # print stus
    # print stus.count()

    # 聚合查询
    # res = models.Student.objects.all().values('age').annotate(c=Count('age')).values('age','c')
    # res = models.Student.objects.all().values('name').annotate(c=Count('name')).values('name', 'c')
    # print res

    # 聚合求平均值
    # res = models.Student.objects.all().values('name').annotate(score_avg=Avg('score'))
    # for item in res:
    #     print item['name'],item['score_avg']

    # 聚合求和
    # res = models.Student.objects.all().values('name').annotate(score_sum=Sum('score'))
    # for item in res:
    #     print item['name'],item['score_sum']

    # res = models.Student.objects.all().values('cls').annotate(score_avg=Avg('score')).values('cls__name','cls__id','score_avg')
    # print res

    # 跨表查询

    stus = models.Student.objects.all()
    for stu in stus:
        print stu.name,stu.age,stu.cls.name,stu.cls.id
    return HttpResponse('ok')

