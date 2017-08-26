from django.conf.urls import include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# urlpatterns = patterns('',
urlpatterns = [
    # Examples:
    # url(r'^$', 'demon.views.home', name='home'),
    # url(r'^demon/', include('demon.foo.urls')),
    url(r'^bilibili/', include('bilibili.urls', namespace='bilibili')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^movies/', include('movies.urls', namespace='movies')),

    url(r'^api/', include('api.urls', namespace='api')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
