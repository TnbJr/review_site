from django.conf.urls import url
from .views import ProfileDetailView, ProfileUpdateView  

urlpatterns = [
	url(r'^(?P<pk>[\d]+)$',  ProfileDetailView.as_view(), name='detail'),
	url(r'^update$',  ProfileUpdateView.as_view(), name='update'),
# 	url(r'^detail/(?P<pk>[\d]+)$',  VideoDetailView.as_view(), name='detail'),

]