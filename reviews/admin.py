from django.contrib import admin
from .models import ProductReview, UserReview

class UserReviewAdmin(admin.ModelAdmin):
	model = UserReview
	list_display = ('product_review', 'user', 'comment', 'rating', 'created')
	list_filter = ['created', 'user']

admin.site.register(ProductReview)
admin.site.register(UserReview, UserReviewAdmin)