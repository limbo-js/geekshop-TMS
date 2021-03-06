from django.shortcuts import render
from django.views.generic import ListView
from .models import *


def index(request):
    return render(request, 'main/index.html')


def shoper(request):
    return render(request, 'main/shoper.html')


class ItemBD(ListView):
    models = Item
    template_name = 'main/catalog.html'
    context_object_name = 'it'

    def get_queryset(self):
        return Item.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
