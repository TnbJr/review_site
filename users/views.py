from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
# Create your views here.


class ProfileDetailView(View):
	def get(self, request, pk):
		instance = get_object_or_404(Profile, pk=pk)
		pass

