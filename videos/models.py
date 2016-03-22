from django.db import models
from embed_video.fields import EmbedVideoField
from django.utils.text import slugify
from django.core.urlresolvers import reverse
# from django.db.models.signals import pre_save
# Create your models here.
class Video(models.Model):
	CATEGORY_CHOICES = (
		("Video-Reviews", "Reviews"),
		("Video", "Video"),

		)
	title = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(unique=True)
	content = models.TextField()
	draft = models.BooleanField(default=False)
	published = models.DateTimeField(auto_now=False, auto_now_add=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	video = EmbedVideoField()
	categories = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="Video")

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("video:detail", kwargs={"pk": self.id})

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
			super(Video, self).save(*args, **kwargs) 
		else:
			super(Video, self).save(*args, **kwargs) 