#coding:utf8
from django.template import Library

register = Library()

@register.simple_tag
def action(path,item,index):
    #print path,item

    url_part = path.split('/')
    if index == 4:
        if url_part[index].split('.')[0] == str(item['id']):
            rep = '<a href="%s" class="active">%s</a>'
        else:
            rep = '<a href="%s">%s</a>'
        url_part[index] = str(item['id']) + '.html'
        url = '/'.join(url_part)
        rep = rep % (url,item['name'])
    else:
        if url_part[index] == str(item.id):
            rep = '<a href="%s" class="active">%s</a>'
        else:
            rep = '<a href="%s">%s</a>'
        url_part[index] = str(item.id)

        url = '/'.join(url_part)
        rep = rep % (url,item.name)
    return rep

@register.simple_tag
def action_all(path,index):
    url_part = path.split('/')
    if index == 4:
        if url_part[index].split('.')[0] == '0':
            rep = '<a href="%s" class="active">全部</a>'
        else:
            rep = '<a href="%s">全部</a>'

        url_part[index] = '0' + '.html'
        url = '/'.join(url_part)
    else:
        if url_part[index] == '0':
            rep = '<a href="%s" class="active">全部</a>'
        else:
            rep = '<a href="%s">全部</a>'

        url_part[index] = '0'
        url = '/'.join(url_part)

    rep = rep % url
    return rep