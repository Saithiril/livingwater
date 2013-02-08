from django.conf.urls import patterns, include, url

urlpatterns = patterns('news.views',
	url(r'^$', 'news'),
	url(r'^add$', 'add'),
	url(r'^addComplete$', 'addComplete'),
	url(r'^(?P<news_id>\d+)/$', 'detail'),
	url(r'^(?P<news_id>\d+)/delete$', 'delete'),
)