#coding:utf8
from django.shortcuts import render,HttpResponseRedirect,HttpResponse

# Create your views here.
import models

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
def manage(request):
    stus = models.Student.objects.all()
    context = {
        'manage' : 'active',
        'stus': stus,
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