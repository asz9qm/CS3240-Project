from django.views.generic import ListView
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Request
from .forms import RequestForm
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from quickthooters import settings
from django.contrib import messages


def get_Request(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        subject = "QuickThooters"
        message = "Hi " + request.user.username + ", Your tutoring request has been submitted !"
        to = request.user.email
        email = send_mail(subject, message, settings.EMAIL_HOST_USER, [to])

        return render(request,'tutor_request/confirmation1.html')
        
    else:
        form = RequestForm({'author':request.user})
        return render(request, 'tutor_request/fill_form.html', {'form': form})


class RequestListHistoryView(ListView):
    model = Request
    template_name = 'tutor_request/requestList.html'
    context_object_name = 'requests'
    paginate_by = 3

    def get_queryset(self):
        return Request.objects.filter(author=self.request.user)


class RequestListView(ListView):
        model = Request
        template_name = 'tutor_request/request.html'
        context_object_name = 'requests'
        paginate_by = 3

        def post(self,request):
            subject = "QuickThooters"
            message = "Hi " + self.request.user.username + ", Your tutoring request has been Accepted !"
            to = self.request.user.email
            email = send_mail(subject, message, settings.EMAIL_HOST_USER, [to])
            return render(self.request, 'tutor_request/confirmation2.html')












