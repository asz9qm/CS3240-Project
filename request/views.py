from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from .models import Request
from django.core.paginator import Paginator
from django.shortcuts import render
from django.core.mail import send_mail
from django.utils import timezone
from quickthooters import settings
from .forms import RequestForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe
from django.views.generic.base import TemplateView


@login_required
def get_Request(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        subject = "QuickThooters"
        message = "Hi " + request.user.username + ", \n\nYour tutoring request has been submitted ! \n\n\nYou will receive a confirmation Email when a tutor accepts your request.\n\n\n\nThank you !\n\n\n\n\nQuickthooters Team"
        to = request.user.email
        email = send_mail(subject, message, settings.EMAIL_HOST_USER, [to])

        return render(request,'tutor_request/confirmation1.html')
        
    else:
        form = RequestForm({'author':request.user})
        return render(request, 'tutor_request/request-new.html', {'form': form})


class RequestListHistoryView(LoginRequiredMixin, ListView):
    model = Request
    template_name = 'tutor_request/request-list-current.html'
    context_object_name = 'requests'
    ordering = ['-date']
    paginate_by = 3


    def get_queryset(self):
        return Request.objects.filter(author=self.request.user)


class RequestListView(LoginRequiredMixin, ListView):
        model = Request
        template_name = 'tutor_request/request-list.html'
        context_object_name = 'requests'
        ordering = ['-date']
        paginate_by = 3

        def get_queryset(self):
            return Request.objects.exclude(author=self.request.user)

        def post(self,request):
            subject = "QuickThooters"
            message = "Hi " + Request.objects.get(pk=request.POST.get('id','default')).author.username + ", \n\nYour tutoring request has been accepted by " + self.request.user.email + " . Please contact your tutor to arrange a meeting time/location.\n\n\nThank you !\n\n\n\n\nQuickthooters team"
            to = Request.objects.get(pk=request.POST.get('id','default')).author.email
            email = send_mail(subject, message, settings.EMAIL_HOST_USER, [to])
            Request.objects.all().filter(pk=request.POST.get('id','default')).delete()
            return render(self.request, 'tutor_request/confirmation2.html')


class RequestDetailView(LoginRequiredMixin, DetailView):
    model = Request
    template_name = 'tutor_request/request-detail.html'


class RequestDeleteView(LoginRequiredMixin, DeleteView):
    model = Request
    template_name = 'tutor_request/request-delete.html'
    success_url = '/'












