from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'508/(?P<username>[\w\._-]+)/$', 'friends_graph.views.friends_graph_508', name='friends_graph_508'),        
    url(r'(?P<username>[\w\._-]+)/$', 'friends_graph.views.friends_graph', name='friends_graph'),    
)
