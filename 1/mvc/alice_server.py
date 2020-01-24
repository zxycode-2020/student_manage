#coding:utf8
from wsgiref.simple_server import make_server
import jinja2
from ctroller import *

# 路由映射信息表
urls = {
    '/' : index,
    '/article' : article,
    '/article_list' : article_list,
}


def application(env,start_response):
    start_response('200 ok', [('Content-Type', 'text/html')])  # 设置响应类型和状态码
    url = env['PATH_INFO']
    # if url == '/':
    #     return index()
    # elif url == '/article':
    #     return article()
    # else:
    #     return '404 page'
    if url in urls.keys():
        fuc = urls.get(url,None)
        if fuc is not None:
            return fuc()
        else:
            return '404'
    else:
        return '404 page'

if __name__ == '__main__':
    http_server = make_server('127.0.0.1',6000,application) #创建httpserver
    http_server.serve_forever() # 启动服务
