from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import Profile
from .forms import ProfileForm
# Create your views here.


class ProfileDetailView(View):
	def get(self, request, pk):
		profile = get_object_or_404(Profile, pk=pk)
		context={
			'queryset': profile.user.username,
			'bio': profile.bio
		}
		return render(request, "profile/profile_detail.html", context)

class ProfileUpdateView(View):
	def get(self, request):
		profile = get_object_or_404(Profile, user=request.user)
		context = {
			'form': ProfileForm(instance=profile)
		}
		return render(request, "profile/profile_detail.html", context)
	
	def post(self, request):
		profile = get_object_or_404(Profile, user=request.user)
		form = ProfileForm(data=request.POST or None, instance=profile)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return redirect('profile:detail', pk=profile.id)
		context = {
			'form': ProfileForm(instance=profile)
		}
		return render(request, "profile/profile_detail.html", context)