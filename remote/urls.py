from django.conf.urls import patterns, url;
from remote import views;

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^index', views.index, name='index'),	
	url(r'^get/(?P<property_name>\w+)/$', views.get_property, name='get_property'),
	url(r'^set/(?P<property_name>\w+)/(?P<property_value>\d+)/$', views.change_property, name='change_property'),
)
