from django.conf.urls import patterns, include, url

from django.contrib import admin

from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'views.home', name='home'),
    # url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-auth/',include('Globe_Mobile_Admin.urls', namespace='globe_rest_framework')),
)
