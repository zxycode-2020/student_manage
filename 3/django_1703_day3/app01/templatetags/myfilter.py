#coding:utf8
from django import template

register = template.Library()

# 自定义过滤器也是一个函数
@register.filter
def disspace(value):
    return value.replace(' ','')
