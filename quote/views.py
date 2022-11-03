from django.shortcuts import render
from django.views import generic, View
from .models import Quote, Item
from django.contrib.auth.models import User

class QuoteList(generic.ListView):
    model = Quote
    queryset = Quote.objects.order_by('-submitted_date')
    template_name = 'index.html'
    paginate_by = 6

class User(generic.ListView):
    model = User
    queryset = User.objects
    template_name = 'user_home.html'