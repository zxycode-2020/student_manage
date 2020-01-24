"""django_1703_day5 URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from GameOfThrone import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index,name='index'),
    url(r'^manage/$', views.manage,name='manage'),
    url(r'^config/$', views.config,name='config'),
    url(r'^stu_del/$', views.stu_del,name='stu_del'),
    url(r'^stu_edit/$', views.stu_edit,name='stu_edit'),
    url(r'^login/$', views.login,name='login'),
    url(r'^reg/$', views.reg,name='reg'),
    url(r'^logout/$', views.logout , name='logout'),
]
