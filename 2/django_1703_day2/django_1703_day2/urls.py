#coding:utf8
"""django_1703_day2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url # 包含url 和 url映射
from django.contrib import admin
from app01.views import index,test,gettime,luping,luping2
from app01 import urls as app01_urls
from app02 import urls as app02_urls
from app03 import urls as app03_urls

# 路由（url）映射信息表
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), #  django默认后台登陆地址
    # name参数给url起别名，在模版中和视图中可以通过别名获取url地址

    url(r'^$', index,name='index'),  #首页路由地址，默认有一个/
    #url(r'^test/$', test ,name='test'),  # 结尾加/好，兼容性强
    #url(r'^test/1702/$',test, name='1702'),
    # url(r'^test/1703/(?P<id1>\d+)/(?P<id2>\d+)/(?P<content>\w+)/$',test, name='1703'),  # 如果有小组则传递给视图函数作为参数
    # url(r'^gettime/$',gettime, name='gettime'),
    # url(r'^luping/$',luping,name='luping'),
    # url(r'^luping2/$',luping2,name='luping2'),
    url(r'^app01/',include(app01_urls,namespace='app01')),
    url(r'^app02/',include(app02_urls,namespace='app02')),
    url(r'^app03/',include(app03_urls,namespace='app03')),
]
