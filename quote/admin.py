from django.contrib import admin
from .models import QuoteData

# @admin.register(Quote)
# class BuckAdmin(admin.ModelAdmin):
#     list_display = ('id', 'quote_name', 'user_id', 'status')
    
# @admin.register(Item)
# class BuckAdmin(admin.ModelAdmin):
#     list_display = ('id', 'quote_id', 'deadline')

@admin.register(QuoteData)
class BuckAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'deadline', 'submitted_date', 'quote_status')
    