from django.views.generic import View
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm

class ContactView(View):
	title = "Contact Us"
	form = ContactForm
	template = "contacts/contact.html"
	confirm_message = None
	def get(self, request):
		context ={
			"title": self.title,
			"form": self.form(request.POST or None),
			'confirm_message': self.confirm_message
		}
		return render(request, self.template, context)

	def post(self, request):
		form = self.form(request.POST or None)
		if form.is_valid():
			name = form.cleaned_data['name']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			emailFrom = form.cleaned_data['email']
			emailTo = [settings.EMAIL_HOST_USER]
			send_mail(subject, message, emailFrom, emailTo, fail_silently=False)
			form.save()
			context={
				"title": "Thanks",
				"confirm_message": "Thanks for the message!",
				"form ": None
			}
			return render(request, self.template, context)
		context ={
		"title": self.title,
		"form": self.form(request.POST or None),
		"confirm_message": self.confirm_message
		}
		return render(request, self.template, context)