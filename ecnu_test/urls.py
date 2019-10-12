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
 
from . import view
 
urlpatterns = [
    url(r'^$', view.index),
    url(r'^info/', view.info),
    #url(r'^save_info/', view.save_info),
    url(r'^intro/', view.intro),#输入用户名信息后交给后台save_info函数处理
    url(r'^warm/', view.warm),
    url(r'^uploadWarm/', view.uploadWarm),
    url(r'^five/', view.five),
    url(r'^six/', view.six),
    url(r'^uploadSix/', view.uploadSix),
    url(r'^seven/', view.seven),
    url(r'^eight/', view.eight),
    url(r'^nine/', view.nine),
    url(r'^ten/', view.ten),
    url(r'^eleven/', view.eleven)
]
