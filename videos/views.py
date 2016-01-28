from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Video 

# Create your views here.

class VideoIndexView(View):
	def get(self, request):
		queryset = Video.objects.all()
		context={
			'queryset': queryset,
		}
		return render(request, "videos/index.html", context)

# class VideoDetailView(View):
# 	def get(self, request, id):
		