from django.contrib.auth.decorators import login_required 
from urllib.parse import quote_plus
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import View
from .models import ContentPost, Category 
from .forms import ContentPostForm

# Create your views here.
class CategoryIndexView(View):
	def get(self, request):
		queryset = Category.objects.all()
		context={
			'queryset_list': queryset
		}
		return render(request, "posts/index.html", context)

class CategoryDetailView(View):
	def get(self, request, slug):
		instance = Category.objects.filter(slug=slug)
		context = {
			"title": slug,
			"instance": instance,
		}
		return render(request, "posts/category_detail.html", context)

class PostIndexView(View):
	def get(self, request):
		queryset_list = ContentPost.objects.all().order_by("-created")
		paginator = Paginator(queryset_list, 10) # Show 25 contacts per page

		page = request.GET.get('page')
		try:
			queryset = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			queryset = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			queryset = paginator.page(paginator.num_pages)


		context = {
			"queryset_list": queryset
		}
		return render(request, "posts/index.html", context)


class PostDetailView(View):
	def get(self, request, slug=None):
		instance = get_object_or_404(ContentPost, slug=slug)
		share_string =quote_plus(instance.title)
		context = {
			"title": instance.title,
			"instance": instance,
			"share_string": share_string
		}
		return render(request, "posts/post_detail.html", context)


class PostCreateView(View):
	def get(self, request):
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
		context = {
			'title': "Create New Content" ,
			'form': ContentPostForm(),
			}
		return render(request, 'posts/post_create.html', context)

	def post(self, request):
		post_form = ContentPostForm(request.POST or None, request.FILES or None)
		if post_form.is_valid():
			instance = post_form.save(commit=False)
			instance.save()
			return redirect('post:index-post')
		context = {
		  'form': compliment_form,
		  }
		return render(request, 'posts/post_create.html', context)

class PostUpdateView(View):
	def get(self, request, slug):
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
		content_post = ContentPost.objects.get(slug=slug)
		context = {
			'title': "Update Content" ,
			'form':ContentPostForm(None, instance=content_post),
			'slug': slug
			}
		return render(request, 'posts/post_update.html', context)
	
	def post(self, request, slug):
		#should add validator to make sure compliment_id is in database
		content_post = get_object_or_404(ContentPost, slug=slug)
		post_form = ContentPostForm(request.POST or None, request.FILES or None, instance=content_post)
		if post_form.is_valid():
			instance = post_form.save(commit=False)
			instance.save()
			return redirect('post:detail', slug=slug)
		context = {
			'form':ContentPostForm(None, instance=content_post),
			'slug': slug
			}
		return render(request, 'posts/post_update.html', context)

class PostDeleteView(View):
	def get(self, request, slug):
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
		context ={
			'title': "Delete Content",
			'slug': slug
		}
		return render(request, 'posts/post_delete.html', context)

	def post(self, request, slug):
		content_post = get_object_or_404(ContentPost, slug=slug)
		content_post.delete()
		return redirect('post:index-post')      
