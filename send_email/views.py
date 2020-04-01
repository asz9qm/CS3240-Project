from django.shortcuts import render
from django.http import HttpResponse
from quickthooters import settings
from django.core.mail import send_mail

def mail(request):
	subject = "QuickThooters Email Test"
	message = "Congratulations !"
	to = "quickthooters@gmail.com"
	email = send_mail(subject, message, settings.EMAIL_HOST_USER, [to])

	if (email == 1):
		message = "Email sent automatically by quickthooters@gmail.com to quickthooters@gmail.com"
	else:
		message = "Email not sent"
	return HttpResponse(message)



