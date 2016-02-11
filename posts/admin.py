from django.contrib import admin
from .models import ContentPost, Category
# Register your models here.
class ContentPostAdmin(admin.ModelAdmin):
	list_display = ["title", "created"]
	# list_display_links = ["email"]
	# list_filter = ["timestamp", "email"]
	search_fields = ["title", "content"]
	exclude = ["slug"]
	# def get_form(self, request, obj=None, **kwargs):
	# 	if obj.type == "1":
	# 		self.exclude = ("slug", )
	# 	form = super(CoontentPostAdmin, self).get_form(request, obj, **kwargs)
	# 	return form 

	class Meta:
		model = ContentPost

	 

admin.site.register(ContentPost, ContentPostAdmin)
admin.site.register(Category)