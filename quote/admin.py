from django.contrib import admin
from .models import Quote, Item

@admin.register(Quote)
class BuckAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'status')
    
@admin.register(Item)
class BuckAdmin(admin.ModelAdmin):
    list_display = ('id', 'quote_id', 'deadline')
    