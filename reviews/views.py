from django.shortcuts import render
from django.contrib import messages
from django.views.generic import View
from django.db.models import Avg
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import ProductReview, UserReview
from .forms import ProductReviewForm, UserReviewForm
from braces.views import StaffuserRequiredMixin
# Create your views here.


class ReviewCategoryView(View):
	template = "reviews/index.html"
	def get(self, request, category):
		queryset = ProductReview.objects.filter(category_slug=category, draft=False, published__lte=timezone.now())
		context = {
			"query_list": queryset,
		}
		return render(request, self.template, context)

class ReviewCreateView(StaffuserRequiredMixin, View):
	template = "reviews/review_create.html"
	form = ProductReviewForm
	title = "Create A New Review"
	def get(self, request):
		context={
			"form": self.form(),
			"title": self.title,
		}
		return render(request, self.template, context)

	def post(self, request):
		form = ProductReviewForm(request.POST or None)
		if form.is_valid():
			instance = form.save()
			return redirect('review:index')
		context={
			"form": self.form(request.POST or None),
			"title": self.title
		}
		return render(request, self.template, context)



class ReviewDeleteView(StaffuserRequiredMixin, View):
	title = "Delete Review"
	template = "reviews/review_delete.html"
	def get(self, request, slug):
		instance = get_object_or_404(ProductReview, slug=slug)
		context = {
			"title": self.title,
			"review": instance.title,
			"slug": slug
		}
		return render(request, self.template, context)

	def post(self, request, pk):
		instance = get_object_or_404(ProductReview, slug=slug)
		instance.delete()
		return redirect('review:index')


class ReviewDetailView(View):
	template = "reviews/review_detail.html"
	form = UserReviewForm
	def get(self, request, slug):
		instance = get_object_or_404(ProductReview, slug=slug)
		user_review = instance.userreview_set.order_by('-created')[:9]
		review_average = UserReview.objects.filter(product_review=instance.id).aggregate(Avg('rating'))
		user_id = request.user.id
		print(request.session)
		context = {
			"title": instance.title,
			"instance": instance,
			"form": self.form(initial={'user': request.user}),
			"average": review_average["rating__avg"],
			"slug": slug,
			"user_id": user_id,
			"user_review": user_review
		}
		return render(request, self.template, context)

	def post(self, request, slug):
		instance = get_object_or_404(ProductReview, slug=slug)
		form = self.form(request.POST or None) 
		if instance.title in request.session:
			messages.error(request, 'You have submitted a review already', fail_silently=True)
			return redirect("review:detail", slug=slug)
		else:
			if form.is_valid():
				form = form.save(commit=False)
				form.user = request.user
				form.product_review = instance
				form.save()
				request.session[instance.title] = instance.title
				return redirect("review:detail", slug=slug)
		context = {
			"title": instance.title,
			"instance": instance,
			"form": self.form(initial={'user': request.user}),
			"average": review_average["rating__avg"],
			"slug": slug,
			"user_id": user_id
		}
		return render(request, self.template, context)


class ReviewIndexView(View):
	template = "reviews/index.html"
	def get(self, request):
		if request.user.is_staff:
			queryset = ProductReview.objects.all()
		else:
			queryset = ProductReview.objects.filter(draft=False, published__lte=timezone.now())
		context={
			"query_list": queryset
		}
		return render(request, self.template, context)


class ReviewUpdateView(StaffuserRequiredMixin, View):
	template = "reviews/review_update.html"
	form = ProductReviewForm
	title = "Update Content"
	def get(self, request, slug):
		instance = get_object_or_404(ProductReview, slug=slug)
		context = {
			"form": self.form(None, instance=instance),
			"title": self.title,
			"slug": slug
		}
		return render(request, self.template, context)

	def post(self, request, pk):
		instance = get_object_or_404(ProductReview, slug=slug)
		form = self.form(request.POST or None, instance=instance)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			return redirect("review:detail", slug=slug)
		context = {
			"form": self.form(request.POST or None),
			"title": self.title,
			"slug": slug
		}
		return render(request, self.template, context)


class UserReviewView(View):
	template = "reviews/users_review.html"
	def get(self, request, pk):
		instance = UserReview.objects.filter(product_review=pk)
		context ={"instance": instance}
		return render(request, self.template, context)

class EditUserReviewView(View):
	template = "reviews/users_review_update.html"
	form = UserReviewForm
	def get(self, request, pk):
		instance = get_object_or_404(UserReview, pk=pk)
		if not request.user.id == instance.user.id:
			raise Http404
		context = {
			"form": self.form(None, instance=instance),
			"pk": pk
		}
		return render(request, self.template, context)

	def post(self, request, pk):
		instance = get_object_or_404(UserReview, pk=pk)
		form = self.form(request.POST or None, instance=instance)
		slug = instance.product_review.slug
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			return redirect("review:detail", slug=slug)
		context = {
			"form": self.form(None, instance=instance),
			"pk": pk
		}
		return render(request, self.template, context)


class DeleteUserReviewView(View):
	title = "Delete Review"
	template = "reviews/users_review_delete.html"
	def get(self, request, pk):
		instance = get_object_or_404(UserReview, pk=pk)
		if not request.user.id == instance.user.id:
			raise Http404
		context = {
			"title": self.title,
			"pk": pk
		}
		return render(request, self.template, context)

	def post(self, request, pk):
		instance = get_object_or_404(UserReview, pk=pk)
		slug = instance.product_review.slug
		title = instance.product_review.title
		instance.delete()
		try:
			del request.session[title]
		except KeyError:
			pass
		return redirect("review:detail", slug=slug)





