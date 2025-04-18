"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#1导入系统的logging
import logging
#2创建日志记录器
logger = logging.getLogger('django')



from django.http import HttpResponse
def log(request):
    #3记录日志
    logger.info('hello world')
    return HttpResponse("<h1>Hello World!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',log),
]
