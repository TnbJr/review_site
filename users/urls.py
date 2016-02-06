from django.conf.urls import url
from .views import ProfileDetailView 

urlpatterns = [
	url(r'^(?P<pk>[\d]+)$',  ProfileDetailView.as_view(), name='detail'),
# 	url(r'^create$',  VideoCreateView.as_view(), name='create'),
# 	url(r'^detail/(?P<pk>[\d]+)$',  VideoDetailView.as_view(), name='detail'),

]