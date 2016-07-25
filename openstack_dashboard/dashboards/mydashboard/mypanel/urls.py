from django.conf.urls import patterns
from django.conf.urls import url

from openstack_dashboard.dashboards.mydashboard.mypanel \
    import views


urlpatterns = patterns('openstack_dashboard.dashboards.mydashboard.mypanel.views',
    url(r'^$',
        views.IndexView.as_view(), name='index'),

#    url(r'^create/$',
#        views.CreateView.as_view(), name='create'),

#    url(r'^(?P<id>[^/]+)/update/$',
#        views.UpdateView.as_view(), name='update'),
)

