from django.conf.urls import url
from .views import VideoIndexView, VideoDetailView, VideoCreateView, VideoUpdateView, VideoDeleteView

urlpatterns = [
	url(r'^$',  VideoIndexView.as_view(), name='index'),
	url(r'^create$',  VideoCreateView.as_view(), name='create'),
	url(r'^detail/(?P<pk>[\d]+)$',  VideoDetailView.as_view(), name='detail'),
	url(r'^update/(?P<pk>[\d]+)$',  VideoUpdateView.as_view(), name='update'),
	url(r'^delete/(?P<pk>[\d]+)$',  VideoDeleteView.as_view(), name='delete'),
	# url(r'^delete/(?P<slug>[\w-]+)$',  PostDeleteView.as_view(), name='delete'),
]