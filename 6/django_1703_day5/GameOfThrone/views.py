#coding:utf8
from django.shortcuts import render,HttpResponseRedirect,HttpResponse

# Create your views here.
from django.db.models import Q  # 单独创建一个查询条件
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.contrib.auth.models import User # 内置用户表
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password # 用户密码加密
from django.contrib.auth.decorators import login_required
from django.contrib import auth

import models

# 学生添加
@login_required
def index(request):
    if request.method == 'POST': # 添加操作
        name = request.POST.get('name',None)
        age = request.POST.get('age',None)
        score = request.POST.get('score',None)
        cid = request.POST.get('cid',None)
        groups = request.POST.getlist('groups') #列表
        stu_info = {
            'name' : name,
            'age' : age,
            'score' : score,
            'cls_id' : cid,
        }
        try:
            s = models.Student.objects.create(**stu_info)
            s.group.add(*groups)
            s.save()
            return HttpResponseRedirect('/manage/')

        except Exception,e:
            return HttpResponse('请好好填写，数据格式不正确，添加失败')

    elif request.method == "GET":
        classes = models.Class.objects.all()
        groups = models.Group.objects.all()
        print groups
        context = {
            'index' : 'active',
            'classes' : classes,
            'groups' : groups,
        }
        return render(request,'homework/index.html',context)

#学生管理
@login_required
def manage(request):
    order = request.GET.get('order',None)
    rule = request.GET.get('rule',None)
    pn = request.GET.get('pn',1)

    try:
        pn = int(pn)
    except:
        pn = 1

    # 搜索
    keyword = request.GET.get('keyword','') 
    if keyword is not None:
        # # 用集合操作符
        # stus1 = models.Student.objects.filter(name__icontains=keyword).all()
        # stus2 = models.Student.objects.filter(age__icontains=keyword).all()
        # stus = stus1 | stus2

        # django 里进行条件合并,组合条件查询
        condition = Q(name__icontains=keyword) | Q(age__icontains=keyword) | Q(cls__name__icontains=keyword)
        stus = models.Student.objects.filter(condition).all()
    else:
        stus = models.Student.objects.all()

    # 排序
    if order is not None: # 排序字段不为空
        if order == '':
            order = 'id'
        if rule == 'up':
            stus = stus.order_by(order) # 升序
        elif rule == 'down':
            stus = stus.order_by('-' + order) #降序

    # 分页
    paginator = Paginator(stus,2) # a1:查询结果集  a2：每页显示记录数
    try:
        stus = paginator.page(pn) # 获取某一页记录
    except (EmptyPage,InvalidPage,PageNotAnInteger) as e:
        pn = 1
        stus = paginator.page(pn)

    # 获取总页数
    num_pages = stus.paginator.num_pages

    # 分页数字实现
    # 显示5个数字，当前页数字放在中间（高亮显示）
    if num_pages >= 5: # 总页数大于你想要显示的分页数字
        if pn <= 2:
            start = 1
            end = 6
        elif pn > num_pages - 2:  # 10页  pn:9
            start = num_pages - 4
            end = num_pages + 1
        else:
            start = pn - 2
            end = pn + 3
    else:
        start = 1
        end = num_pages + 1

    numbers = range(start , end)

    context = {
        'manage' : 'active',
        'stus': stus,
        'num_pages' : num_pages,
        'numbers' : numbers,
        'pn' : pn,
    }
    return render(request,'homework/manage.html',context)

def config(request):
    context = {
        'config' : 'active'
    }
    return render(request,'homework/config.html',context)

def stu_del(request):
    # 获取学生id
    sid = request.GET.get('sid',None)
    if sid is not None:
        sid = int(sid)
        res = models.Student.objects.filter(id=sid).delete()
        if res != 0:
            return HttpResponseRedirect('/manage/')
        else:
            return HttpResponse('删除失败，数据异常')
    else:
        return HttpResponse('数据异常')

def stu_edit(request):
    sid = request.GET.get('sid', None) #  获取学生id
    stu = models.Student.objects.get(pk=sid)  # 获取修改哪个学生

    if request.method == 'POST': # 修改操作
        name = request.POST.get('name',None)
        age = request.POST.get('age',None)
        score = request.POST.get('score',None)
        cid = request.POST.get('cid',None)
        groups = request.POST.getlist('groups') #列表
        stu_info = {
            'name' : name,
            'age' : age,
            'score' : score,
            'cls_id' : cid,
        }
        try:
            res = models.Student.objects.filter(pk=sid).update(**stu_info)
            if res != 0:
                stu.group.clear()
                stu.group.add(*groups)
                return HttpResponseRedirect('/manage/')
            else:
                return HttpResponse('修改失败')

        except Exception,e:
            print e
            return HttpResponse('请好好填写，数据格式不正确，修改失败')

    elif request.method == "GET":

        classes = models.Class.objects.all() # 所有班级
        groups = models.Group.objects.all() # 所有小组

        # 上下文字典
        context = {
            'classes' : classes,
            'groups' : groups,
            'stu': stu,
        }
        return render(request,'homework/edit.html',context)

# 用户登陆业务逻辑处理
def login(request):
    if request.method == 'POST':
        error = ''
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        # print username,password
        if username and password: # 验证用户名和密码是否为空
            user = auth.authenticate(username=username,password=password) #如果验证成功，返回用户实例.不成功返回None
            if user is not None: # 用户存在
                if user.is_active: # 判断用户是否激活状态
                    # 用户登陆
                    auth.login(request,user)
                    # 登陆成功
                    to_url = reverse('manage')
                    return HttpResponseRedirect(to_url)
            else:
                error = '用户名或密码错误'
                return render(request,'user/login.html',{'error':error})

        else:
            error = '用户名或密码不能为空'
            return render(request,'user/login.html',{'error' : error})

    elif request.method == 'GET':
        return render(request,'user/login.html')

# 用户注册
def reg(request):
    # 获取用户注册信息
    username = request.POST.get('username',None)
    password1 = request.POST.get('password1',None)
    password2 = request.POST.get('password2',None)
    nick = request.POST.get('nick','匿名')
    qq = request.POST.get('qq','')
    phone = request.POST.get('phone','')

    if username and password1 and password2: #有点不能为空
        if password1 == password2: # 密码确认验证
            uc = User.objects.filter(username=username).all().count() # 验证用户名是否存在
            if uc == 0: #用户名不存在
                user_info = {
                    'username' : username,
                    'password' : make_password(password1),
                    'is_active' : 1,
                    'is_superuser' : 0,
                    'is_staff' : 1,
                }
                # 插入django内置用户表
                user = User.objects.create(**user_info)

                # 插入用户扩展信息表
                profile_info = {
                    'nick' : nick,
                    'user' : user,
                    'qq' : qq,
                    'phone' : phone,
                }
                try:
                    models.UserProfile.objects.create(**profile_info)
                    # 注册成功 则跳转
                    to_url = reverse('login')
                    return HttpResponseRedirect(to_url)

                except Exception,e:
                    error = '系统繁忙'
                    return render(request, 'user/reg.html', {'error': error})

            else:
                #用户名存在
                error = '用户名已被注册，想一个更好的吧，你太low了'
                return render(request, 'user/reg.html', {'error': error})
        else:
            error = '两次密码不相同'
            return render(request, 'user/reg.html', {'error': error})
    else:
        error = '用户名密码不能为空'
        return render(request,'user/reg.html',{'error':error})

# 用户退出
def logout(request):
    auth.logout(request)
    to_url = reverse('login')
    return HttpResponseRedirect(to_url)