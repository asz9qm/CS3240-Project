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


class RequestView(generic.CreateView):
    model = Request
    fields = ('subject', 'location', 'specific')
    template_name = 'tutor_request/request.html'

class RequestList(generic.ListView):
    model = Request
    template_name = 'tutor_request/requestList.html'

def get_Request(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        post = form.save(commit=False)
        post.save()
        subject = "QuickThooters"
        message = "Hi " + request.user.username + ", Your tutoring request has been submitted !"
        to = request.user.email
        email = send_mail(subject, message, settings.EMAIL_HOST_USER, [to])
        
        
        if (email == 1):
            message = "Confirmation email sent !"
        else:
            message = "Unable to send confirmation email ! call support..."

        return HttpResponse(message)
        
    else:
        form = RequestForm()

    return render(request, 'tutor_request/request.html', {'form': form})

class DetailView(generic.DetailView):
    model = Request
    template_name = 'tutor_request/detail.html'
   

class Accept(DeleteView):
    model = Request
    success_url = ("/../..")
    template_name = 'tutor_request/accept.html'





