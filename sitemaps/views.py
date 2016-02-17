from django.shortcuts import render, redirect 
from django.views.generic import View
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from itertools import chain
from operator import attrgetter
from newsletters.forms import SignUpForm
from posts.models import ContentPost
from reviews.models import ProductReview
from videos.models import Video 


# Create your views here.
class IndexView(View):
	def query_chain(self):
			post_queryset = ContentPost.objects.filter(draft=False, published__lte=timezone.now())
			review_queryset = ProductReview.objects.filter(draft=False, published__lte=timezone.now())
			video_queryset = Video.objects.filter(draft=False, published__lte=timezone.now())
			result_query = sorted(
				chain(post_queryset, review_queryset, video_queryset),
				key=attrgetter('published'), reverse=True)
			return result_query

	def get(self, request):
		page_template = 'post.html'
		template = 'index.html'
		form = SignUpForm(request.POST or None)
		query = self.query_chain()
		paginator = Paginator(query, 5) # Show 10 contacts per page
		print(paginator.num_pages)
		print(request.GET)
		# if request.is_ajax():
		# 	template = page_template
		page = request.GET.get('page')
		try:
			queryset = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			queryset = paginator.page(1)
		except EmptyPage:
			if request.is_ajax():
				print(request.GET)
				return HttpResponse('')
			# If page is out of range (e.g. 9999), deliver last page of results.
			queryset = paginator.page(paginator.num_pages)
		context = {
			"form": form,
			"query": queryset
		}
		if request.is_ajax():
			return render(request, page_template, context)
		return render(request, template, context)

	def post(self, request):
		form = SignUpForm(request.POST or None)
		context = {
		"form": form, 
		}
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return redirect('sitemaps:share')
		return render(request, 'index.html', context)
	
class AboutView(View):
	def get(self, request):
		return render(request, 'sitemaps/about.html')
		
class ShareView(View):
	def get(self, request):
		return render(request, 'sitemaps/share.html')
