from django.conf.urls import include, url

import views

urlpatterns = [
    url('^$',views.index),
    url('^cal/$',views.cal),
    url('^reg/$',views.reg),
    url('^login/$',views.login)
]
