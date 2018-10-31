# from django.conf.urls import url, include
from django.urls import path
from basic_app import views

#Template tagging
app_name = 'basic_app'

urlpatterns=[
    # url(r'^$',views.index,name='index'),
    # url(r'^other/$',views.other,name='other'),
    # url(r'^relative/$',views.relative,name='relative'),
    path('',views.index,name='index'),
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
]