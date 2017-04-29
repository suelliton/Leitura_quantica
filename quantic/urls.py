from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$',views.home),
	url(r'^login$',views.login),
	url(r'^register_user$',views.register_user),
	url(r'^user$',views.user),
	url(r'^index$',views.index),
	url(r'^home$',views.home),
	url(r'^logout$',views.logout),
	url(r'^edit_user$',views.edit_user),




]
