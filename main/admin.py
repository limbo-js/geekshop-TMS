from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'coast', 'amount', 'image')
    fields = ('name', 'coast', 'amount', 'text', 'image')
