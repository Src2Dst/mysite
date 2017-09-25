from django.conf.urls import include, url
from django.contrib import admin
#import app
from mainsite import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^index/', views.Index),
]
