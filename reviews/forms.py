from django import forms
from .models import ProductReview, UserReview

class ProductReviewForm(forms.ModelForm):
	class Meta:
		model = ProductReview
		fields = [ 'name',
					'draft'
				]

class UserReviewForm(forms.ModelForm):
	class Meta:
		model = UserReview
		fields = [ 'user_name',
					'comment',
					'rating'
				]