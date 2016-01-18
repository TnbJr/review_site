from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm

class ContactView(View):
	def get(self, request):
		form = ContactForm(request.POST or None)
		title = 'Contact Us'
		title_align_center = True
		confirm_message = None
		template = 'contact.html'
		context ={
		"title": title,
		"form": form,
		"title_align_center": title_align_center,
		'confirm_message': confirm_message
		}
		return render(request, 'contacts/contact.html', context)

	def post(self, request):
		form = ContactForm(request.POST or None)
		title = 'Contact Us'
		title_align_center = True
		confirm_message = None
		if form.is_valid():
			name = form.cleaned_data['name']
			subject = 'Message from EasyDabble.com'
			message = form.cleaned_data['message']
			emailFrom = form.cleaned_data['email']
			emailTo = [settings.EMAIL_HOST_USER]
			send_mail(subject, message, emailFrom, emailTo, fail_silently=False)
			title = "Thanks"
			confirm_message = "Thanks for the message!"
			form = None
		context ={
		"title": title,
		"form": form,
		"title_align_center": title_align_center,
		'confirm_message': confirm_message
		}

		return render(request, 'contacts/contact.html', context)

# def contact(request):
# 	title = 'Contact Us'
# 	title_align_center = True
# 	form = contactForm(request.POST or None)
# 	confirm_message = None
# 	if form.is_valid():
# 		name = form.cleaned_data['name']
# 		subject = 'Message from EasyDabble.com'
# 		message = form.cleaned_data['message']
# 		emailFrom = form.cleaned_data['email']
# 		emailTo = [settings.EMAIL_HOST_USER]
# 		send_mail(subject, message, emailFrom, emailTo, fail_silently=False)
# 		title = "Thanks"
# 		confirm_message = "Thanks for the message!"
# 		form = None
# 	context ={
# 		"title": title,
# 		"form": form,
# 		"title_align_center": title_align_center,
# 		'confirm_message': confirm_message
# 		}
# 	template = 'contact.html'
# 	return render(request, template, context)