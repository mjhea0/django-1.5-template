from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^login', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}, name='login'),
	url(r'^logout', 'django.contrib.auth.views.logout', {'next_page': '/login'}),
	url(r'^register', 'users.views.register', name='register'),
	url(r'^.*$', 'dash.views.index', name='home'),
)
