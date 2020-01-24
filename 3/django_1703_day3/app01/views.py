#coding:utf8
from django.shortcuts import render,HttpResponse,render_to_response
import logging
from django.template import Template,Context
import datetime

# Create your views here.
#创建一个日志器
mylogger = logging.getLogger('app01')

class Human(object):
    name = '人'
    age = 10000

    def sayGoodBye(self):
        #return 回去的值就是模板中显示的值
        return 'sayGoodBye-------------'


# def index(request):
#     try:
#         with open('wer','r') as f:
#             f.read()
#     except Exception,e:
#         mylogger.error(str(e))
#     return HttpResponse('app01 index page ok')

def index(request):
    return render(request,'app01/index.html')

def zhale(request):
    mylogger.critical('洗澡城炸了')
    return HttpResponse('ok')

def tpl(request):
    # --------------------------------------------------------------------
    t = Template("<h1>My name is {{name}}.</h1>") # 一小段html 加载到Template里，返回Template对象
    context = {'name' : 'Alice'} # 上下文字典，准备渲染到模版中的变量
    c = Context(context) # 初始化一个Context对象 传入上下文字典
    html = t.render(c) # 渲染模板，选入Context对象
    # --------------------------------------------------------------------

    # render_to_response 不需要传入request对象，
    # render需要
    # return render_to_response('app01/tpl.html')

    # 上下文字典
    h1 = Human()

    context = {
        'name' : '小美',
        'engname' : 'XIAOMEI',
        'age' : 18,
        'sex' : '中',
        'score' : 100.99,
        #'subject' : ['python','php','java','hadoop','openstack','docker','c++'],
        'subject' : [],
        'info' : {'interest':'打游戏','money':0},
        'h1' : h1,
        'china' : [
            {'北京' : ['朝阳','海淀',u'三里屯','什刹海','中南海','天安门','changping']},
            {'黑龙江' : ['哈尔滨','牡丹江','齐齐哈尔','鸡西','日本','首尔','俄罗斯']},
        ],
        'range': range(1,11),
        'desc' : "了矿务局儿科就了哦字。， \n想，臭美吧厘米",
        'desc1' : "how are old you",
        'now' : datetime.datetime.now(),
        'suibian' : None,
        'link' : '<a href="http://www.baidu.com">点我</a>'

    }
    return render(request,'app01/tpl.html',context)  # a1：request对象，a2：模板路径  a3：上下文字典