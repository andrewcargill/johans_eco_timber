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
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView


# class QuoteList(generic.ListView):
#     model = QuoteData
#     template_name = 'index.html'
#     paginate_by = 6

class QuoteList(TemplateView):
    template_name = 'index.html'


class About(generic.ListView):
    model = QuoteData
    template_name = 'about.html'
    paginate_by = 6


class AboutEnquiry(generic.ListView):
    model = QuoteData
    template_name = 'about_enquiry_system.html'


class Forest(generic.ListView):
    model = QuoteData
    template_name = 'ourforest.html'


class QuoteUpdate(SuccessMessageMixin, UpdateView):
    model = QuoteData
    template_name_suffix = '_edit_form'
    form_class = QuoteForm
    success_message = "Enquiry successfully updated! Submit to receive a quote"

    def get_success_url(self):
        return reverse("quote_list")


class QuoteDelete(SuccessMessageMixin, DeleteView):
    model = QuoteData
    template_name_suffix = '_confirm_delete'
    success_message = "Enquiry successfully updated!"
    success_url = reverse_lazy("quote_list")


class UserQuoteList(ListView):
    model = QuoteData
    context_object_name = "quote_list"
    template_name = 'quote_list.html'

    def get_queryset(self):
        return QuoteData.objects.filter(
            user_id=self.request.user).order_by("status")


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
            quote.status = 1
            quote.save()
            messages.add_message(
                request, messages.INFO, 
                "Thank you for submitting your enquiry! Expect an email within 24hrs"
                )
            return HttpResponseRedirect(reverse('quote_list'))


def QuoteInput(request):
    print("-------GETTING CALLED")
    print(request.method)

    if request.method == 'POST':
        print("-------POST is True")
        # create a form instance and populate it with data from the request:
        form = QuoteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user_id = request.user  # The logged-in user
            quote.save()
            messages.add_message(
                request, messages.INFO, 
                'Enquiry Saved! Submit to receive a quote'
                )
            response = redirect('quote_list.html')
            return response
            print("-------form is valid")
    else:
        print("-------form is NOT valid")
        form = QuoteForm()
        
    return render(request, 'new_enquiry.html', {'form': form})


def NewItem(request):
    print("-------GETTING CALLED")
    print(request.method)
    
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

