from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic.edit import UpdateView, DeleteView
from django.views import generic, View
from django.views.generic import ListView
from .models import QuoteData
from django.contrib.auth.models import User
from .forms import QuoteForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.forms import TextInput
from django.urls import reverse_lazy



class QuoteList(generic.ListView):
    model = QuoteData
    template_name = 'index.html'
    paginate_by = 6


#New for single quote database

class QuoteUpdate(UpdateView):
    model = QuoteData
    template_name_suffix = 'form'
    form_class = QuoteForm

    def get_success_url(self):
        return reverse("quote_list")


class QuoteDelete(DeleteView):
    model = QuoteData
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy("quote_list")


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
            "quote_submit.html",
            {
                "quote": quote,
            }
        )

    def post(self, request, id):
        if request.method == 'POST':
            print("Ready to submit")
            quote = QuoteData.objects.get(id=id)
            quote.quote_status = "Submitted"
            quote.save()
            
        def get_success_url(self):
            return reverse("quote_list")



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

      
