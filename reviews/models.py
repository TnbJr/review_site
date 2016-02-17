from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class ProductReview(models.Model):
	CATEGORY_CHOICES = (
		("Desktop Vaporizer", "Desk"),
		("Handheld Vaporizer", "Hand"),
		("Other", "Other"),
		)
	title = models.CharField(max_length=150)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now = True)
	draft = models.BooleanField(default=False)
	published = models.DateTimeField(auto_now_add=False, auto_now=False)
	affiliate_link = models.URLField(null=True, blank=True)
	# slug = models.SlugField()
	categories = models.CharField(max_length=50, choices=CATEGORY_CHOICES)


	def get_absolute_url(self):
		return reverse("review:detail", kwargs={"pk": self.id})

	def __str__(self):
		return self.title 

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
	comment = models.CharField(max_length=255)
	rating = models.IntegerField(choices=RATING_CHOICES)
	created = models.DateTimeField(auto_now_add=True)