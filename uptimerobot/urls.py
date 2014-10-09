"""URLs for the uptimerobot app."""
try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url
 


urlpatterns = patterns('', 
    url(r'^$', 'uptimerobot.views.index', name='uptimerobot_index'),
)
