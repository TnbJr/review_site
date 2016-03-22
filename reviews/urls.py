from django.conf.urls import url
from .views import ReviewIndexView, ReviewCreateView, ReviewDetailView, ReviewUpdateView, ReviewDeleteView, UserReviewView, EditUserReviewView, DeleteUserReviewView

urlpatterns = [
	url(r'^$',  ReviewIndexView.as_view(), name='index'),
	url(r'^create/$',  ReviewCreateView.as_view(), name='create'),
	url(r'^(?P<slug>[\w-]+)$',  ReviewDetailView.as_view(), name='detail'),
	url(r'^update/(?P<slug>[\w-]+)$',  ReviewUpdateView.as_view(), name='update'),
	url(r'^delete/(?P<slug>[\w-]+)$',  ReviewDeleteView.as_view(), name='delete'),
	url(r'^user-reviews/(?P<pk>[\d]+)$',  UserReviewView.as_view(), name='user-reviews'),
	url(r'^edit-user-reviews/(?P<pk>[\d]+)$',  EditUserReviewView.as_view(), name='edit-user-reviews'),
	url(r'^delete-user-reviews/(?P<pk>[\d]+)$',  DeleteUserReviewView.as_view(), name='delete-user-reviews'),
]