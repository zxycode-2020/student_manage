#coding:utf8
from django.shortcuts import HttpResponse,render,HttpResponseRedirect,render_to_response
import datetime

# Create your views here.

def index(request): # request 获取http请求信息
    return HttpResponse('app01 index page ok') # 响应基类 响应一段字符串

def test(request,id1,id2,content):
    print type(id1),type(id2),type(content) # 参数全部是unicode类型，如果想当整型来用则需要转换
    print id1,id1,content
    return HttpResponse('test page ok')

def gettime(request):
    # 获取服务器时间格式化字符串
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(now)

def luping(request):
    return HttpResponse('luping')

def luping2(request):
    return HttpResponse('luping222222222222')