from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^spools/', include('spools.urls', namespace="spools")),
    url(r'^admin/', include(admin.site.urls)),
)
