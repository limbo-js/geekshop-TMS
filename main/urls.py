from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('catalog/', ItemBD.as_view(), name='catalog'),
    path('shoper/', shoper, name='shoper')
]
