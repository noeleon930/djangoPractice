from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangoTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'noel.views.hello_world'),
    url(r'^hello2/$', 'noel2.views.hello_world'),
    url(r'^helloUrl/(?P<name>.+)/', 'unicodeTest.views.helloUrl'),
    url(r'^$', 'noel.views.home'),
]
