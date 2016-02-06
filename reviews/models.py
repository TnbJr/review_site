from django.db import models
from django.core.urlresolvers import reverse

class ProductReview(models.Model):
	name = models.CharField(max_length=150)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now = True)
	draft = models.BooleanField(default=False)
	published = models.DateTimeField(auto_now_add=False, auto_now=False)


	def get_absolute_url(self):
		return reverse("review:detail", kwargs={"pk": self.id})

	def __str__(self):
		return self.name 

class UserReview(models.Model):
	RATING_CHOICES = (
		(1, '1'),
		(2, '2'),
		(3, '3'),
		(4, '4'),
		(5, '5'),
		)
	product_review = models.ForeignKey(ProductReview)
	user_name = models.CharField(max_length=150)
	comment = models.CharField(max_length=255)
	rating = models.IntegerField(choices=RATING_CHOICES)
	created = models.DateTimeField(auto_now_add=True)