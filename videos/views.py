from django.shortcuts import render
from django.http import Http404
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Video 
from .forms import VideoForm

# Create your views here.

class VideoIndexView(View):
	def get(self, request):
		queryset = Video.objects.all()
		context={
			'queryset': queryset,
		}
		return render(request, "videos/index.html", context)

class VideoDetailView(View):
	def get(self, request, pk):
		instance = get_object_or_404(Video, pk=pk)
		context = {
			"title": instance.title,
			"instance": instance
		}
		return render(request, "videos/video_detail.html", context)

class VideoCreateView(View):
	def get(self, request):
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
		context = {
			'form': VideoForm()
		}
		return render(request, 'videos/video_create.html', context)

	def post(self, request):
		video_form =VideoForm(data=request.POST or None)
		if video_form.is_valid():
			instance = video_form.save(commit=False)
			instance.save()
			return redirect('video:index')
			context = {
				'form': video_form
			}
		return render(request, 'videos/video_create', context)

class VideoUpdateView(View):
	def get(self, request, pk):
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
		video_post = get_object_or_404(Video, pk=pk)
		context = {
			'form': VideoForm(instance=video_post),
			'pk': video_post.id
		}
		return render(request, 'videos/video_update.html', context)

	def post(self, request, pk):
		video_post = get_object_or_404(Video, pk=pk)
		video_form = VideoForm(data=request.POST or None, instance=video_post)
		if video_form.is_valid():
			instance = video_form.save(commit=False)
			instance.save()
			return redirect('video:detail', pk=pk)
		context = {
			'form': video_form,
			'pk': video_post.id
		}
		return render(request, 'videos/video_update.html', context)

