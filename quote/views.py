from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import UpdateView
from django.views import generic, View
from django.views.generic import ListView
from .models import Quote, Item, QuoteData
from django.contrib.auth.models import User
from .forms import NameForm, AddItem, QuoteForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect



class QuoteList(generic.ListView):
    model = Quote
    queryset = Quote.objects.order_by('-submitted_date')
    template_name = 'index.html'
    paginate_by = 6


#New for single quote database

class QuoteUpdate(UpdateView):
    model = QuoteData
    fields = '__all__'
    template_name_suffix = 'form'
    

class UserQuoteList(ListView):
    model = QuoteData
    # queryset = QuoteData.objects.filter(status=0)
    context_object_name = "quote_list"
    template_name = 'quote_list.html'
    def get_queryset(self):
        return QuoteData.objects.filter(user_id=self.request.user)

class QuoteDetail(View):

    def get(self, request, id, *args, **kwargs):
        quote = QuoteData.objects.get(id=id)

        return render(
            request,
            "quote_edit.html",
            {
                "quote": quote,
            }
        )



# class UserQuoteList(ListView):
#     model = QuoteData
#     queryset = QuoteData.objects.filter(status=0)
#     context_object_name = "quote_list"
#     template_name = 'quote_list.html'
    



def QuoteInput(request):
    print("-------GETTING CALLED")
    print(request.method)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("-------POST is True")
        # create a form instance and populate it with data from the request:
        form = QuoteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user_id = request.user  # The logged-in user
            quote.save()
            response = redirect('quote_list.html')
            return response
            print("-------form is valid")
    else:
        print("-------form is NOT valid")
        form = QuoteForm()

    return render(request, 'user_home.html', {'form': form})

##Original user_home quote entry

# def get_name(request):
#     print("-------GETTING CALLED")
#     print(request.method)
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         print("-------POST is True")
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             quote = form.save(commit=False)
#             quote.user_id = request.user  # The logged-in user
#             quote.save()
#             response = redirect('add_item.html')
#             return response
#             print("-------form is valid")
            
            # form.save()
            # return HttpResponseRedirect('user_home.html')

    # if a GET (or any other method) we'll create a blank form
    # else:
    #     print("-------form is NOT valid")
    #     form = NameForm()

    #  return render(request, 'user_home.html', {'form': form})

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

      
