"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add_stuff'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^category/(?P<category_id>.+)/$', views.render_category, name='category'),
    url(r'^category/(?P<category_id>.+)/add$', views.render_add_sub, name='add_sub'),
    url(r'^category/(?P<category_id>.+)/add/submit$', views.render_add_sub_ack, name='add_sub_submit'),
    url(r'^deletesub/(?P<subcategory_id>.+)/$', views.delete_sub, name='deletesub'),
    
]
