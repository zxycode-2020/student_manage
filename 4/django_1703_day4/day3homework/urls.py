from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^manage/$', views.manage,name='manage'),
    url(r'^config/$', views.config,name='config'),
]
