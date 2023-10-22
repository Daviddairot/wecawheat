from django.contrib import admin
from .models import Item
# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_image', 'description')
    list_filter = ('title', 'content_image', 'description')
    search_fields = ('title', 'content_image', 'description')
