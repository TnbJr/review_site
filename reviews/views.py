from django.shortcuts import render
from django.views.generic import View
from django.db.models import Avg
from django.shortcuts import render, redirect, get_object_or_404
from .models import ProductReview, UserReview
from .forms import ProductReviewForm, UserReviewForm
# Create your views here.


class ReviewIndexView(View):
	def get(self, request):
		queryset = ProductReview.objects.all()
		context={
			'query_list': queryset
		}
		return render(request, "reviews/index.html", context)

class ReviewCreateView(View):
	def get(self, request):
		context={
			'form': ProductReviewForm()
		}
		return render(request, "reviews/review_create.html", context)

	def post(self, request):
		form = ProductReviewForm(request.POST or None)
		if form.is_valid():
			instance = form.save()
			return redirect('review:index')
		context={
			'form': form
		}
		return render(request, "reviews/index.html", context)

class ReviewDetailView(View):
	def get(self, request, pk):
		instance = get_object_or_404(ProductReview, pk=pk)
		omg = UserReview.objects.filter(product_review=pk).aggregate(Avg('rating'))
		form = UserReviewForm()
		context = {
			"title": instance.name,
			"instance": instance,
			"form": form,
			"omg": omg["rating__avg"]
		}
		return render(request, "reviews/review_detail.html", context)
