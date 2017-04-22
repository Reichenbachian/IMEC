from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'api/getSearchResults/$', views.getSearchResults),
	url(r'^$', views.index, name='index'),
	url(r'^scan$', views.scan, name='scan'),
	url(r'^search$', views.search, name='search'),
	url(r'^test', views.test, name='test'),
]
