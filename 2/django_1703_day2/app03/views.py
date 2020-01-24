#coding:utf8
from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    print request.user # 获取请求用户,没有登陆就是匿名用户
    print request.path # 请求路径
    print request.get_full_path() # 请求的uri（路径+查询参数）
    print request.get_host() # 主机地址
    print request.method # http请求类型（GET （查询操作是get请求），POST（一般情况是增删改操作））
    #print request.POST # 获取post提交过来的所有参数

    # 获取Get查询参数
    print request.GET # 获取get提交过来的所有参数
    a = request.GET.get('a',None)
    b = request.GET.get('b',None)
    print request.GET.getlist('a')
    print request.GET.getlist('b')

    # 获取post查询参数
    return HttpResponse('app03 index page ok')

# 登陆页
def login(request):
    # 处理的GET请求
    if request.method == 'POST':
        print request.POST
        return HttpResponse('data submit ok')
    elif request.method == 'GET': # get请求则渲染登陆表单
        return render(request,'app03/login.html')

# 注册页
def reg(request):
    # 处理的GET请求
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        gender = request.POST.get('gender',None)
        interest = request.POST.getlist('interest')
        cls = request.POST.get('cls')
        print username,password,gender,cls
        print interest

        if username and password:
            # 操作数据库
            return HttpResponse('注册成功')
        else:
            return HttpResponse('用户名或密码不能为空')

    elif request.method == 'GET': # get请求则渲染登陆表单
        return render(request,'app03/reg.html')
