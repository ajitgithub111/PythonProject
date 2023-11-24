from django.shortcuts import render
from .models import pythonmodel
from django.views.generic import CreateView,ListView,DetailView,DeleteView,TemplateView,UpdateView

# Create your views here.


class pyform(CreateView):
    model = pythonmodel
    template_name = 'python/pyform.html'
    fields = "__all__"
    success_url = '/wcem/temp/'

class pytem(TemplateView):
    model=pythonmodel
    template_name = 'python/tems.html'