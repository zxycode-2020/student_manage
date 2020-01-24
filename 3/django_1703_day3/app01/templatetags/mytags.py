#coding:utf8
from django import template
import datetime
register = template.Library()

#自定义标签,一个标签是一个函数
@register.simple_tag
def add(v1,v2):
    return v1 + v2 #有return返回

@register.simple_tag
def get_now():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


