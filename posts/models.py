from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify 
from django.utils import timezone 




class ContentPost(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(unique=True)
	image = models.ImageField(null=True, blank=True,
		width_field="width_field",
		height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	content = models.TextField()
	draft = models.BooleanField(default=False)
	published = models.DateTimeField(auto_now=False, auto_now_add=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	categories = models.ManyToManyField('Category') 
	default = models.ForeignKey('Category', related_name='default_category', null=True, blank=True)
	

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse("post:detail", kwargs={"slug": self.slug})
		# return "/article/%s/" %(self.id)models fro

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
			super().save(*args, **kwargs)
		else:
			super().save(*args, **kwargs)

	class Meta:
		ordering = ['-created']
			
class Category(models.Model):
	title = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(unique=True)
	description = models.CharField(max_length=255)
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse("post:detail-category", kwargs={"slug": self.slug})

	#Creates a slug if one is not present 
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
			super().save(*args, **kwargs)
		else:
			super().save(*args, **kwargs)
# def create_slug(instance, new_slug=None):
# 	slug = slugify(instance.title)
# 	if new_slug is not None:
# 		slug = new_slug
# 	qs = ContentPost.objects.filter(slug=slug).order_by("-id")
# 	exists = qs.exists()
# 	if exists:
# 		new_slug = "%s-%s" %(slug, qs.first().id)
# 		return create_slug(instance, new_slug=new_slug)
# 	return slug


# def pre_save_post_receiver(sender, instance, *args, **kwargs):
# 	if not instance.slug:
# 		instance.slug = create_slug(instance)


# pre_save.connect(pre_save_post_receiver, sender=ContentPost)