from django import forms

# class QuoteForm(forms.Form):
#     text = forms.CharField()

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
