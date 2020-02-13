from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse


class IndexView(generic.DetailView):
    def get(self, request):
        return HttpResponse("Dis the index")
