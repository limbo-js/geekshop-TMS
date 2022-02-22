from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator
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

# <def catalog(request, EmptyPage=None, PageNotAnInteger=None):
#   page = request.GET.get('page')
#    try:
#        item = paginator.page(page)
#    except PageNotAnInteger:
#        item = paginator.page(1)
#    except EmptyPage:
#        item = paginator.page(paginator.num_pages)
#    return render(request, 'main/catalog.html', {'page': page, 'item': item, })
