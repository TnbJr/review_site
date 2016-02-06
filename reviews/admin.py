from django.contrib import admin
from .models import ProductReview, UserReview

class UserReviewAdmin(admin.ModelAdmin):
	model = UserReview
	list_display = ('product_review', 'user_name', 'comment', 'rating', 'created')
	list_filter = ['created', 'user_name']

admin.site.register(ProductReview)
admin.site.register(UserReview, UserReviewAdmin)