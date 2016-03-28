from django.conf.urls import url
from .views import VideoCategoryView

urlpatterns = [
	url(r'^(?P<category>[\w-]+)$',  VideoCategoryView.as_view(), name='category'),
]