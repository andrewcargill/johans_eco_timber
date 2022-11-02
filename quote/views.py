from django.shortcuts import render
from django.views import generic, View
from .models import Quote, Item

class QuoteList(generic.ListView):
    model = Quote
    queryset = Quote.objects.order_by('-submitted_date')
    template_name = 'index.html'
    paginate_by = 6