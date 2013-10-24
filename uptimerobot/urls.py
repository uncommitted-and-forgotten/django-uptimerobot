"""URLs for the uptimerobot app."""
from django.conf.urls.defaults import patterns, url
 


urlpatterns = patterns('', 
    url(r'^$', 'uptimerobot.views.index', name='uptimerobot_index'),
)
