from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LivinWater.views.home', name='home'),
    # url(r'^LivinWater/', include('LivinWater.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'LivinWater.views.index'),
	url(r'^home$', 'LivinWater.views.index'),
	url(r'^registration$', 'LivinWater.views.registration'),
	url(r'^login$', 'LivinWater.views.login'),
	url(r'^logout$', 'LivinWater.views.logout'),
	url(r'^auth$', 'LivinWater.views.authorization'),
	url(r'^signup$', 'LivinWater.views.signup'),
	url(r'^manage$', 'LivinWater.views.manage'),
	url(r'^manage/users$', 'LivinWater.views.user_list'),
	url(r'^manage/users/(?P<user_id>\d+)/$', 'LivinWater.views.user_info_by_id'),
	url(r'^manage/groups$', 'LivinWater.views.groups_list'),
	url(r'^manage/groups/add$', 'LivinWater.views.group_add'),
	url(r'^manage/add_group$', 'LivinWater.views.add_group'),
	url(r'^news/', include('news.urls')),
	url(r'^user/info/$', 'LivinWater.views.user_info'),
	url(r'^user/edit$', 'LivinWater.views.user_edit'),
)

urlpatterns += patterns('',
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'./media/'}),
)