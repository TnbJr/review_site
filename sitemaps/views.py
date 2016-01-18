from django.shortcuts import render, redirect 
from django.views.generic import View
from newsletters.forms import SignUpForm
# from .forms import UserForm
# from .models import User 

# Create your views here.
class IndexView(View):
	def get(self, request):
		form = SignUpForm(request.POST or None)
		context = {
		"form": form,
		}
		return render(request, 'index.html', context)

	def post(self, request):
		form = SignUpForm(request.POST or None)
		context = {
		"form": form, }
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
