from django.shortcuts import render
from django.views import generic, View
from django.views.generic import TemplateView
from .models import Quote, Item
from django.contrib.auth.models import User
from .forms import NameForm
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
            print("-------form is valid")
            
            # form.save()
            # return HttpResponseRedirect('user_home.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        print("-------form is NOT valid")
        form = NameForm()

    return render(request, 'user_home.html', {'form': form})



# class User(generic.ListView):
#     model = User
#     queryset = User.objects
#     template_name = 'user_home.html'





