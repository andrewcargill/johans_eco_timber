from django.contrib import admin
from .models import QuoteData

@admin.register(QuoteData)
class BuckAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'deadline', 'submitted_date', 'status',)
    