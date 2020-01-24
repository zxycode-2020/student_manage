from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'add/', views.add),
    url(r'delete/', views.delete),
    url(r'update/', views.update),
    url(r'select/', views.select),
]