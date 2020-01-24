from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'test1/$', views.test_redirect,name='test_redirect'),
    url(r'new_test/$', views.new_test,name='new_test'),
]
