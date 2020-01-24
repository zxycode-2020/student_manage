"""kamiedu URL Configuration

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
from home import views as home_views
from django.views.static import serve
from django.conf import settings
import os

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_views.index,name='index'),
    url(r'^student/$', home_views.student,name='student'),
    url(r'^upload/(.*)', serve,{'document_root': os.path.join(settings.BASE_DIR,'upload')}),
]
