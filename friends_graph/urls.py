from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^(?P<username>[\w\._-]+)/$', 'friends_graph.views.friends_graph', name='friends_graph'),    
)
