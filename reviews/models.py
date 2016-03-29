from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify 
from taggit.managers import TaggableManager


class ProductReview(models.Model):
	CATEGORY_CHOICES = (
		("Desktop Vaporizer", "Desk"),
		("Handheld Vaporizer", "Hand"),
		("Other", "Other"),
		)
	RATING_CHOICES = (
		(1, '1'),
		(2, '2'),
		(3, '3'),
		(4, '4'),
		(5, '5'),
		)
	title = models.CharField(max_length=150, unique=True)
	slug = models.SlugField()
	image = models.ImageField(null=True, blank=True)
	rating  = models.IntegerField(choices=RATING_CHOICES)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now = True)
	draft = models.BooleanField(default=False)
	published = models.DateTimeField(auto_now_add=False, auto_now=False)
	source = models.URLField(null=True, blank=True)
	affiliate_link = models.URLField(null=True, blank=True)
	categories = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
	featured = models.BooleanField(default=False)
	tags = TaggableManager() 
	category_slug = models.SlugField()
	convenience = models.CharField(max_length=100, null=True, blank=True)
	concentrate_only = models.CharField(max_length=100, null=True, blank=True)
	product_dimensions = models.CharField(max_length=100, null=True, blank=True)
	

	def get_absolute_url(self):
		return reverse("review:detail", kwargs={"slug": self.slug})

	def get_section_url(self):
		return reverse("review-category:category", kwargs={"category": self.category_slug})

	def save(self, *args, **kwargs):
		if not self.slug or not self.category_slug:
			self.slug = slugify(self.title)
			self.category_slug = slugify(self.categories)
			super().save(*args, **kwargs)
		else:
			super().save(*args, **kwargs)

	def __str__(self):
		return self.title 

	class Meta:
		ordering = ['-created']

class UserReview(models.Model):
	RATING_CHOICES = (
		(1, '1'),
		(2, '2'),
		(3, '3'),
		(4, '4'),
		(5, '5'),
		)
	product_review = models.ForeignKey(ProductReview)
	user = models.ForeignKey(User)
	comment = models.TextField()
	rating = models.IntegerField(choices=RATING_CHOICES)
	created = models.DateTimeField(auto_now_add=True)