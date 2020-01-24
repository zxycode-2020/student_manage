#coding:utf8
from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('homework ok')

def cal(request):
    if request.method == 'POST':
        num1 = request.POST.get('num1',None)
        num2 = request.POST.get('num2',None)
        operation = request.POST.get('operation',None)
        expression = num1 + operation + num2
        try:
            return HttpResponse(eval(expression))
        except Exception,e:
            return HttpResponse('操作符异常')
        # num1 = int(num1)
        # num2 = int(num2)
        # if operation == '+':
        #     return HttpResponse(num1 + num2)
        # elif operation == '-':
        #     return HttpResponse(num1 - num2)
        # else:
        #     return HttpResponse('操作异常')
    else:
        return render(request,'homework/cal.html')

def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        username = username.encode('utf-8')
        password = password.encode('utf-8')

        if username and password:
            with open('user.txt','a') as f:
                f.write(username + ' ' + password + '\n')
            return HttpResponse('注册成功')
        else:
            return HttpResponse('不能为空')
    else:
        return render(request,'homework/reg.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        username = username.encode('utf-8')
        password = password.encode('utf-8')
        user = username + ' ' + password + '\n'
        if username and password:
            with open('user.txt','r') as f:
                user_list = f.readlines()   # ['dachui 123\n']
                if user in user_list:
                    return HttpResponse('登陆成功')
                else:
                    return HttpResponse('用户名密码错误')
        else:
            return HttpResponse('不能为空')
    else:
        return render(request,'homework/login.html')
