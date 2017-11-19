# -*- coding: utf-8 -*-

from django.conf.urls import url

from images import views as images_views

urlpatterns = [
	url(r'^create/$', images_views.image_create, name = 'create'),
	url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', images_views.image_detail, name = 'detail'),
]
