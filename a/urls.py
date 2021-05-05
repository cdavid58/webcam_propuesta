from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^$',home,name="home"),
		url(r'^servicios/$',servicios,name="servicios"),
		url(r'^contacto/$',contacto,name="contacto"),		
	]