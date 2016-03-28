from django.shortcuts import render, redirect 
from django.views.generic import View
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from itertools import chain
from operator import attrgetter
from newsletters.forms import SignUpForm
from reviews.models import ProductReview
#combines quersets from diffrent tables
from .utils import query_chain

# Create your views here.
class IndexView(View):
	def get(self, request):
		page_template = 'post.html'
		template = 'index.html'
		form = SignUpForm(request.POST or None)
		query = query_chain()
		featured_item = ProductReview.objects.filter(featured=True)
		paginator = Paginator(query, 5) # Show 10 contacts per page
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
			"signup_form": form,
			"query": queryset,
			"main_featured": featured_item.first(), 
			"other_featured": featured_item[1:5],
		}
		if request.is_ajax():
			return render(request, page_template, context)
		return render(request, template, context)


	
class AboutView(View):
	def get(self, request):
		return render(request, 'sitemaps/about.html')
		
class ShareView(View):
	def get(self, request):
		return render(request, 'sitemaps/share.html')
