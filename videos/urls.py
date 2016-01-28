from django.conf.urls import url
from .views import VideoIndexView

urlpatterns = [
	url(r'^$',  VideoIndexView.as_view(), name='index-video'),
	# url(r'^create$',  PostCreateView.as_view(), name='create'),
	# url(r'^detail/(?P<slug>[\w-]+)$',  PostDetailView.as_view(), name='detail'),
	# url(r'^update/(?P<slug>[\w-]+)$',  PostUpdateView.as_view(), name='update'),
	# url(r'^delete/(?P<slug>[\w-]+)$',  PostDeleteView.as_view(), name='delete'),
	# url(r'^category$',  CategoryIndexView.as_view(), name='index-category'),
	# url(r'^category1/(?P<slug>[\w-]+)$',  CategoryDetailView.as_view(), name='detail-category'),
]