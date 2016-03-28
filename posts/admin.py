from django.contrib import admin
from .models import ContentPost
# Register your models here.
class ContentPostAdmin(admin.ModelAdmin):
	list_display = ["title", "created"]
	# list_display_links = ["email"]
	# list_filter = ["timestamp", "email"]
	search_fields = ["title", "content"]
	exclude = ["slug"]

	class Meta:
		model = ContentPost

	 

admin.site.register(ContentPost, ContentPostAdmin)
