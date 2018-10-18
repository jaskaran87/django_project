from django.conf.urls import url
from .views  import *

urlpatterns = [ 
	url(r'^$', cart_home, name = 'home'),
	url(r'^update/$', cart_update, name='update')
]