from django.conf.urls import include, url
from .views import IndexView, AboutView, ShareView

urlpatterns = [
	url(r'^$',  IndexView.as_view(), name='index'),
	url(r'^about$',  AboutView.as_view(), name='about'),
	url(r'^share$', ShareView.as_view(), name='share'),
]