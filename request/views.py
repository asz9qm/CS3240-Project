from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Request
from .forms import RequestForm
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from quickthooters import settings
from django.contrib import messages


def get_Request(request):
    if request.method == "POST":
        author = request.user
        form = RequestForm(request.POST)
        post = form.save(commit=False)
        post.save()
        subject = "QuickThooters"
        message = "Hi " + request.user.username + ", Your tutoring request has been submitted !"
        to = request.user.email
        email = send_mail(subject, message, settings.EMAIL_HOST_USER, [to])
        
        
        if (email == 1):
            messages.success(request, f'A confirmation Email was sent !')
        else:
            messages.success(request, f'Unable to send confirmation Email, please contact support !')

        return redirect('/')
        
    else:
        form = RequestForm()
        return render(request, 'tutor_request/fill_form.html', {'form': form})

def  request_list(request):
    context = {

        'requests': Request.objects.all().filter(author=request.user)

        }

    return render(request, 'tutor_request/requestList.html', context)


def all_requests(request):

    if request.method == "POST":

        subject = "QuickThooters"
        message = "Hi " + request.user.username + ", Your tutoring request has been Accepted !"
        to = request.user.email
        email = send_mail(subject, message, settings.EMAIL_HOST_USER, [to])

        return redirect('/')

    else:
    
        context = {

                'requests' : Request.objects.all()
         }

        return render(request,'tutor_request/request.html', context)











