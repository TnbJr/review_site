from django.conf.urls import url
from .views import ReviewIndexView, ReviewCreateView, ReviewDetailView

urlpatterns = [
	url(r'^$',  ReviewIndexView.as_view(), name='index'),
	url(r'^create/$',  ReviewCreateView.as_view(), name='create'),
	url(r'^reviews/(?P<pk>[\d]+)$',  ReviewDetailView.as_view(), name='detail'),
	# url(r'^$',  ReviewIndexView.as_view(), name='delete'),
]
