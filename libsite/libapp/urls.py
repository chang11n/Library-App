from django.conf.urls import url
from . import views
import os
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^(?P<item_id>\d+)/$', views.detail, name='detail'),
    url(r'^suggestions$', views.suggestions, name='suggestions'),
    url(r'^newitem$', views.newitem, name='newitem'),
    url(r'^searchlib$',views.searchlib, name='searchilib'),
    url(r'^result$', views.result, name='result'),
    url(r'^login$', views.user_login, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^myitems$', views.myitems, name='myitems'),
    url(r'^register$', views.register, name='register'),

]

