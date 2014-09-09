from django.conf.urls import patterns, include, url

from django.contrib import admin
from pest.views import pest,index
from news.views import news_detail,news,trend
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Foodyleaks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    #url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    #url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.article_detail),
    url(r'^$', index),
    url(r'^trend/', trend), 
    url(r'^news/detail/(?P<news_id>[0-9]+)', news_detail),
    url(r'^news/', news),  
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pest/', pest),
    
)
