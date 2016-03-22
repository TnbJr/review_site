from django.conf.urls import url
from .views import ReviewCategoryView

urlpatterns = [
	url(r'^(?P<category>[\w-]+)$',  ReviewCategoryView.as_view(), name='category'),
]