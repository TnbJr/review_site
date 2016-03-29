from django.shortcuts import render
from django.http import Http404
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote_plus
from braces.views import StaffuserRequiredMixin
from .models import Video 
from .forms import VideoForm

class VideoCategoryView(View):
	template = "videos/index.html"
	def get(self, request, category):
		queryset_list = Video.objects.filter(category_slug=category, draft=False, published__lte=timezone.now())
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
			"queryset": queryset
		}
		return render(request, self.template, context)

class VideoIndexView(View):
	template = "videos/index.html"
	title = "Video"
	def get(self, request):
		if request.user.is_staff:
			queryset_list = Video.objects.all()
		else:
			queryset_list = Video.objects.filter(draft=False, published__lte=timezone.now())
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

		context={
			"queryset": queryset,
		}
		return render(request, self.template, context)

class VideoDetailView(View):
	template = "videos/video_detail.html"
	def get(self, request, pk):
		instance = get_object_or_404(Video, pk=pk)
		share_string = quote_plus(instance.title)
		context = {
			"title": instance.title,
			"instance": instance,
			"pk": instance.id,
			"share_string": share_string

		}
		return render(request, self.template, context)

class VideoCreateView(StaffuserRequiredMixin, View):
	template = "videos/video_create.html"
	form = VideoForm
	title = "Create A New Video Post"
	def get(self, request):
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
		context = {
			"form": VideoForm(),
			"title": self.title
		}
		return render(request, self.template, context)

	def post(self, request):
		form = self.form(data=request.POST or None)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			return redirect('video:index')
		context = {
			"form": self.form(data=request.POST or None),
			"title": self.title
			}
		return render(request, self.template, context)

class VideoUpdateView(StaffuserRequiredMixin, View):
	template = "videos/video_update.html"
	form = VideoForm
	def get(self, request, pk):
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
		video_post = get_object_or_404(Video, pk=pk)
		context = {
			'form': self.form(instance=video_post),
			'pk': video_post.id
		}
		return render(request, self.template, context)

	def post(self, request, pk):
		video_post = get_object_or_404(Video, pk=pk)
		form = self.form(data=request.POST or None, instance=video_post)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			return redirect('video:detail', pk=pk)
		context = {
			'form': self.form(request.POST or None),
			'pk': video_post.id
		}
		return render(request, self.template, context)

class VideoDeleteView(StaffuserRequiredMixin, View):
	title = "Delete Video"
	template = "videos/video_delete.html"
	def get(self, request, pk):
		video_post = get_object_or_404(Video, pk=pk)
		context ={
			"title": self.title,
			"pk": pk
		}
		return render(request, self.template, context)

	def post(self,request,pk):
		video_post = get_object_or_404(Video, pk=pk)
		video_post.delete()
		return redirect('video:index')

