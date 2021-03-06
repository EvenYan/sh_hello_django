from django.conf.urls import url
from one.views import *


urlpatterns = [
    url(r'^index1/$', index1, name='index1'),
    url(r'^index2/$', index2, name='index2'),
    url(r'^home/$', home),
    url(r'^get_data/$', get_data),
    url(r'^register/$', register, name='register'),
    url(r'^api_v1_save_data/$', save_data, name='save_data'),
    url(r'^static/$', static),
    url(r'^detail/(\d+)/$', detail, name='detail'),
    url(r'^login/$', login, name='login'),
    url(r'^deal_login/$', deal_login, name='deal_login'),
]
