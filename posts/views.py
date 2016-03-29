from django.views.generic import View
from django.http import Http404
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render,redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote_plus
from django.utils import timezone
from braces.views import StaffuserRequiredMixin
from .forms import ContentPostForm
from .models import ContentPost

# Create your views here.
class CategoryIndexView(StaffuserRequiredMixin, View):
	template = "posts/index.html"
	def get(self, request):
		queryset = ContentPost.objects.all()
		context={
			"queryset": queryset
		}
		return render(request, self.template, context)

class CategoryDetailView(View):
	template = "posts/category_detail.html"
	def get(self, request, slug):
		queryset_list = ContentPost.objects.filter(categories=slug, draft=False, published__lte=timezone.now())
		if not queryset_list:
			raise Http404
		
		paginator = Paginator(queryset_list, 2) # Show 10 contacts per page

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
			"title": slug,
			"queryset": queryset,
		}
		return render(request, self.template, context)


class PostCreateView(StaffuserRequiredMixin, View):
	title = "Create New Content"
	template = "posts/post_create.html"
	form = ContentPostForm
	def get(self, request):
		context = {
			'title': self.title,
			'form': self.form(),
			}
		return render(request, self.template, context)

	def post(self, request):
		post_form = self.form(request.POST or None, request.FILES or None)
		if post_form.is_valid():
			instance = post_form.save(commit=False)
			instance.save()
			return redirect('post:index-post')
		context = {
			"title": self.title,
		  	"form": self.form(request.POST or None, request.FILES or None),
		  }
		return render(request, self.template, context)


class PostDeleteView(StaffuserRequiredMixin, View):
	template = "posts/post_delete.html"
	def get(self, request, slug):
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
		context ={
			"title": "Delete Content",
			"slug": slug
		}
		return render(request, self.template, context)

	def post(self, request, slug):
		content_post = get_object_or_404(ContentPost, slug=slug)
		content_post.delete()
		return redirect('post:index-post') 

class PostDetailView(View):
	template = "posts/post_detail.html"
	def get(self, request, slug=None):
		instance = get_object_or_404(ContentPost, slug=slug)
		if instance.published > timezone.now():
			if not request.user.is_staff or not request.user.is_superuser:
				raise Http404
		share_string = quote_plus(instance.title)
		context = {
			"title": instance.title,
			"instance": instance,
			"share_string": share_string
		}
		return render(request, self.template, context)

class PostIndexView(View):
	template = "posts/index.html"
	def get(self, request):
		today = timezone.now().date()
		if request.user.is_staff:
			queryset_list = ContentPost.objects.all()
		else:
			queryset_list = ContentPost.objects.filter(draft=False, published__lte=timezone.now())
		paginator = Paginator(queryset_list, 2) # Show 10 contacts per page

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
			"queryset": queryset,
			"today": today,
		}
		return render(request, self.template, context)


class PostUpdateView(StaffuserRequiredMixin, View):
	title = "Update Content"
	template = "posts/post_update.html"
	form = ContentPostForm
	def get(self, request, slug):
		content_post = get_object_or_404(ContentPost, slug=slug)
		context = {
			"title":  self.title,
			"form": self.form(None, instance=content_post),
			"slug": slug
			}
		return render(request, self.template, context)
	
	def post(self, request, slug):
		content_post = get_object_or_404(ContentPost, slug=slug)
		post_form = self.form(request.POST or None, request.FILES or None, instance=content_post)
		if post_form.is_valid():
			instance = post_form.save(commit=False)
			instance.save()
			return redirect('post:detail', slug=slug)
		context = {
			"title": self.title,
			"form": self.form(None, instance=content_post),
			"slug": slug
			}
		return render(request, self.template, context)
     
