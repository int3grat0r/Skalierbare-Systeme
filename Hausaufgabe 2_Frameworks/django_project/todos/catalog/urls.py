"""todos URL Configuration

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

"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
"""

from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls import *

from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name ='index'),
    path('page_edit_task/', views.page_edit_task, name ='page_edit_task'),
    path('page_new_task/', views.page_new_task, name ='page_new_task'),
    path('page_impressum/', views.page_impressum, name ='page_impressum'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name='delete'),
    path('page_new_task/', views.page_new_task, name='page_new_task'),]


