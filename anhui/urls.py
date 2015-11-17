from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from views import test
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite5.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('model.urls')),
    url(r'^test/',test),
    (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_URL}),
                
)
