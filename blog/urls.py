from django.conf.urls import patterns, url, include
from . import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	#url(r'^$',views.post_list, name='post_list'),
	url(r'^post/list/$', views.post_list, name='post_list'),
	url(r'^$', views.home, name='home'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url('', include('social.apps.django_app.urls', namespace='social')),
	url('', include('django.contrib.auth.urls', namespace='auth'))
	)

# urlpatterns = patterns('',
   # url(r'^$', 'views.home', name='home'),
   # url(r'^admin/', include(admin.site.urls)),
# )