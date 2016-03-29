from django.db import models
from embed_video.fields import EmbedVideoField
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

class Video(models.Model):
	CATEGORY_CHOICES = (
		("video-reviews", "Reviews"),
		("video", "Video"),

		)
	title = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(unique=True)
	content = models.TextField()
	draft = models.BooleanField(default=False)
	published = models.DateTimeField(auto_now=False, auto_now_add=False)
	source = models.URLField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	video = EmbedVideoField()
	categories = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="Video")
	category_slug = models.SlugField()
	tags = TaggableManager() 
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("video:detail", kwargs={"pk": self.id})

	def get_section_url(self):
		return reverse("video-category:category", kwargs={"category": self.category_slug})

	def save(self, *args, **kwargs):
		if not self.slug or not self.category_slug:
			self.slug = slugify(self.title)
			self.category_slug = slugify(self.categories)
			super(Video, self).save(*args, **kwargs) 
		else:
			super(Video, self).save(*args, **kwargs) 