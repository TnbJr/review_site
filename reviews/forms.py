from django import forms
from .models import ProductReview, UserReview

class ProductReviewForm(forms.ModelForm):
	class Meta:
		model = ProductReview
		fields = [ 'name',
					'review',
					'published',
					'affiliate_link',
					'draft'
				]

class UserReviewForm(forms.ModelForm):
	class Meta:
		model = UserReview
		fields = [ 'user',
					'comment',
					'rating'
				]