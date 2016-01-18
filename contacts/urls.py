from django.conf.urls import include, url
from .views import ContactView

urlpatterns = [
	url(r'^$',  ContactView.as_view(), name='contact'),
]