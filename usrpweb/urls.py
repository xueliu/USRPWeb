from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^remote/', include('remote.urls')),
)
