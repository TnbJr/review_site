from django.contrib import admin
from .models import ProductReview, UserReview

class UserReviewAdmin(admin.ModelAdmin):
	model = UserReview
	list_display = ('product_review', 'user', 'comment', 'rating', 'created')
	list_filter = ['created', 'user']
	# 

class ProductReviewAdmin(admin.ModelAdmin):
	model = UserReview
	list_display = ('title', 'created', 'updated', 'categories')
	list_filter = ['title', 'created', 'updated', 'categories']
	exclude = ["slug", "category_slug"]


admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(UserReview, UserReviewAdmin)