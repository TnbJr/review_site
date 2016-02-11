from django.conf.urls import url
from .views import ReviewIndexView, ReviewCreateView, ReviewDetailView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
	url(r'^$',  ReviewIndexView.as_view(), name='index'),
	url(r'^create/$',  ReviewCreateView.as_view(), name='create'),
	url(r'^reviews/(?P<pk>[\d]+)$',  ReviewDetailView.as_view(), name='detail'),
	url(r'^update/(?P<pk>[\d]+)$',  ReviewUpdateView.as_view(), name='update'),
	url(r'^delete/(?P<pk>[\d]+)$',  ReviewDeleteView.as_view(), name='delete'),
]