from django import forms
from .models import Profile

class ContentPostForm(forms.Form):
	title = forms.CharField()
	

	# class Meta:
	# 	model = Profile
		# fields = ['title',
		# 		'image',
		# 		 'content',
		# 		 'draft',
		# 		 'published'
		# 		 ]

	def save(self, user):
		pass