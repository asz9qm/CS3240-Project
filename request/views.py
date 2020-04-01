from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Request
from .forms import RequestForm
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect
# Create your views here.

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
        return redirect('./list')
    else:
        form = RequestForm()

    return render(request, 'tutor_request/request.html', {'form': form})

class DetailView(generic.DetailView):
    model = Request
    template_name = 'tutor_request/detail.html'
    # def get_queryset(self):       
    #     return self

class Accept(DeleteView):
    model = Request
    success_url = ("/../..")
    template_name = 'tutor_request/accept.html'





