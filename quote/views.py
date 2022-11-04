from django.shortcuts import render
from django.views import generic, View
from django.views.generic import TemplateView
from .models import Quote, Item
from django.contrib.auth.models import User
from .forms import QuoteForm


class QuoteList(generic.ListView):
    model = Quote
    queryset = Quote.objects.order_by('-submitted_date')
    template_name = 'index.html'
    paginate_by = 6

# class User(generic.ListView):
#     model = User
#     queryset = User.objects
#     template_name = 'user_home.html'

class User(TemplateView):
    model = User
    queryset = User.objects
    template_name = 'user_home.html'

    def get(self, request):
        form = QuoteForm()
        return render(request, self.template_name, {'form': form})