from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
from .models import Request
from django.core.paginator import Paginator
from django.shortcuts import render
from django.core.mail import send_mail
from django.utils import timezone
from quickthooters import settings
from .forms import RequestForm



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
        return render(request, 'tutor_request/request-new.html', {'form': form})


class RequestListHistoryView(ListView):
    model = Request
    template_name = 'tutor_request/request-list-current.html'
    context_object_name = 'requests'
    ordering = ['-date']
    paginate_by = 3

    def get_queryset(self):
        return Request.objects.filter(author=self.request.user)


class RequestListView(ListView):
        model = Request
        template_name = 'tutor_request/request-list.html'
        context_object_name = 'requests'
        ordering = ['-date']
        paginate_by = 3

        def post(self,request):
            subject = "QuickThooters"
            message = "Hi " + Request.objects.get(pk=request.POST.get('id','default')).author.username + ", Your tutoring request has been Accepted !"
            to = Request.objects.get(pk=request.POST.get('id','default')).author.email
            email = send_mail(subject, message, settings.EMAIL_HOST_USER, [to])
            Request.objects.all().filter(pk=request.POST.get('id','default')).delete()
            return render(self.request, 'tutor_request/confirmation2.html')


class RequestDetailView(DetailView):
    model = Request
    template_name = 'tutor_request/request-detail.html'


class RequestDeleteView(DeleteView):
    model = Request
    template_name = 'tutor_request/request-delete.html'
    success_url = '/'











