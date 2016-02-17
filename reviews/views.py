from django.shortcuts import render
from django.views.generic import View
from django.db.models import Avg
from django.shortcuts import render, redirect, get_object_or_404
from .models import ProductReview, UserReview
from .forms import ProductReviewForm, UserReviewForm
# Create your views here.


class ReviewIndexView(View):
	template = "reviews/index.html"
	def get(self, request):
		queryset = ProductReview.objects.all()
		context={
			"query_list": queryset
		}
		return render(request, self.template, context)

class ReviewCreateView(View):
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

class ReviewDetailView(View):
	template = "reviews/review_detail.html"
	form = UserReviewForm
	def get(self, request, pk):
		instance = get_object_or_404(ProductReview, pk=pk)
		review_average = UserReview.objects.filter(product_review=pk).aggregate(Avg('rating'))
		user_id = request.user.id
		context = {
			"title": instance.title,
			"instance": instance,
			"form": self.form(initial={'user': request.user}),
			"average": review_average["rating__avg"],
			"pk": pk,
			"user_id": user_id
		}
		return render(request, self.template, context)

	def post(self, request, pk):
		instance = get_object_or_404(ProductReview, pk=pk)
		form = self.form(request.POST or None)
		print(instance)
		print(form)
		if form.is_valid():
			form = form.save(commit=False)
			form.user = request.user
			form.product_review = instance
			form.save()
			return redirect("review:detail", pk=pk)
		context = {
			"title": instance.title,
			"instance": instance,
			"form": self.form(initial={'user': request.user}),
			"average": review_average["rating__avg"],
			"pk": pk,
			"user_id": user_id
		}
		return render(request, self.template, context)


class ReviewUpdateView(View):
	template = "reviews/review_update.html"
	form = ProductReviewForm
	title = "Update Content"
	def get(self, request, pk):
		instance = get_object_or_404(ProductReview, pk=pk)
		context = {
			"form": self.form(None, instance=instance),
			"title": self.title,
			"pk": pk
		}
		return render(request, self.template, context)

	def post(self, request, pk):
		instance = get_object_or_404(ProductReview, pk=pk)
		form = self.form(request.POST or None, instance=instance)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			return redirect("review:detail", pk=pk)
		context = {
			"form": self.form(request.POST or None),
			"title": self.title,
			"pk": pk
		}
		return render(request, self.template, context)

class ReviewDeleteView(View):
	title = "Delete Review"
	template = "reviews/review_delete.html"
	def get(self, request, pk):
		instance = get_object_or_404(ProductReview, pk=pk)
		context = {
			"title": self.title,
			"review": instance.name,
			"pk": pk
		}
		return render(request, self.template, context)

	def post(self, request, pk):
		instance = get_object_or_404(ProductReview, pk=pk)
		instance.delete()
		return redirect('review:index')

# class CommentCreateView(View):
# 	form = UserReviewForm
# 	def post(self, request, pk):
# 		instance = get_object_or_404(ProductReview, pk=pk)
# 		form = self.form(request.POST or None, initial={'user': request.user})
# 		if form.is_valid():
# 			form = form.save(commit=False)
# 			form.save()
# 			return("review:detail", pk=pk)



