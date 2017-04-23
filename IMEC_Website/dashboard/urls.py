from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'api/getSearchResults/$', views.getSearchResults),
	url(r'^$', views.index),
	url(r'^scan/$', views.scan),
	url(r'^search/$', views.search),
	url(r'^login/', views.login_page),
	url(r'^employee/', views.employeeHome),
	url(r'^test/', views.test),
]
