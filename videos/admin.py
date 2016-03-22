from django.contrib import admin
from .models import Video
# Register your models here.


class VideoAdmin(admin.ModelAdmin):
	list_display = ("title", "created", "updated", )
	list_filter = ["title", "created", "updated" ]
	exclude = ["slug"]
	class Meta:
		model = Video

admin.site.register(Video, VideoAdmin)
