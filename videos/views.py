from django.shortcuts import render
from django.http import Http404
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Video 
from .forms import VideoForm

# Create your views here.

class VideoIndexView(View):
	template = "videos/index.html"
	title = "Video"
	def get(self, request):
		queryset = Video.objects.all()
		context={
			"queryset": queryset,
			"title": self.title
		}
		return render(request, self.template, context)

class VideoDetailView(View):
	template = "videos/video_detail.html"
	def get(self, request, pk):
		instance = get_object_or_404(Video, pk=pk)
		context = {
			"title": instance.title,
			"instance": instance
		}
		return render(request, self.template, context)

class VideoCreateView(View):
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

class VideoUpdateView(View):
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

class VideoDeleteView(View):
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

