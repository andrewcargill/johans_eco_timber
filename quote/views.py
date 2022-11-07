from django.shortcuts import render, redirect
from django.views import generic, View
from django.views.generic import TemplateView
from .models import Quote, Item
from django.contrib.auth.models import User
from .forms import NameForm, AddItem
from django.core.mail import send_mail
from django.http import HttpResponseRedirect



class QuoteList(generic.ListView):
    model = Quote
    queryset = Quote.objects.order_by('-submitted_date')
    template_name = 'index.html'
    paginate_by = 6


def get_name(request):
    print("-------GETTING CALLED")
    print(request.method)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("-------POST is True")
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user_id = request.user  # The logged-in user
            quote.save()
            response = redirect('add_item.html')
            return response
            print("-------form is valid")
            
            # form.save()
            # return HttpResponseRedirect('user_home.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        print("-------form is NOT valid")
        form = NameForm()

    return render(request, 'user_home.html', {'form': form})

def NewItem(request):
    print("-------GETTING CALLED")
    print(request.method)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("-------POST is True")
        # create a form instance and populate it with data from the request:
        form = AddItem(request.POST)

        # check whether it's valid:
        if form.is_valid():
            form.save()
    else:
        print("-------form is NOT valid")
        form = AddItem()

    return render(request, 'add_item.html', {'form': form})