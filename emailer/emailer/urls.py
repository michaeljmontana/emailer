from django.conf.urls import patterns, include, url
from emailer import views
urlpatterns = patterns('',
                       url(r'^$','sendmails.views.home'),
                       url(r'^sendmails/',include('sendmails.urls')),
                                                    
                                                    
                                              
                                      )


