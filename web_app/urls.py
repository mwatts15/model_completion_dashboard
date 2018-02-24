"""channelworm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.urls import re_path
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin

from modelcompletion.views import index


urlpatterns = [
    re_path(r'^auth/', include('django.contrib.auth.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^index$', index),
    re_path(r'^pyopenworm/',
            include(('modelcompletion.urls', 'whatsanappname'), namespace="modelcompletion"),),
    re_path(r'^pyopenworm/api/',
            include(('modelcompletion.api.urls', 'idk'),
                    namespace="modelcompletion-api"),),

    re_path(r'^$', index, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
