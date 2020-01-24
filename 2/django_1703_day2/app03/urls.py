from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'login/$', views.login,name='login'),
    url(r'reg/$', views.reg,name='reg'),
]
