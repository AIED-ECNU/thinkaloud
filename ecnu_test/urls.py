"""ecnu_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from myapp import views
from django.contrib import admin
from django.views import static 
from django.conf import settings 

 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^info/', views.info),
    #url(r'^save_info/', views.save_info),
    url(r'^intro/', views.intro),#输入用户名信息后交给后台save_info函数处理
    url(r'^warm/', views.warm),
    url(r'^uploadWarm/', views.uploadWarm),
    url(r'^five/', views.five),
    url(r'^eight/', views.eight),
    url(r'^uploadEight/', views.uploadEight),
    url(r'^six/',views.six),
    url(r'^uploadSix/', views.uploadSix),
    url(r'^seven/',views.seven),
    url(r'^search/',views.search),
    url(r'^nine/',views.nine),
    url(r'^ten/',views.ten),
    url(r'^final/',views.final),
    url(r'^static/(?P<path>.*)$', static.serve,
      {'document_root': settings.STATIC_ROOT}, name='static'),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
