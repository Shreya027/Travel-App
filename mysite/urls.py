"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from mysite.views import hello,current_datetime,hours_ahead
from travel import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^search/$', views.search),
    url(r'^contact/$',views.contact),
    url(r'^list/$',views.list),
    url(r'^map/$',views.map),
    url(r'^hotel/$',views.hotel),
    url(r'^direction/$',views.direction),
    url(r'^quiz/$',views.quiz),
    url(r'^currency/$',views.currency),
    url(r'^country/$',views.country),
    url(r'^index/$',views.index),


               #  url(r'^search-form/$', views.search_form),
               #url(r'^search/$', views.search),
               #url(r'^contact/$', contact),
]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



