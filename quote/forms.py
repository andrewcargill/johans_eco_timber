from django import forms

class QuoteForm(forms.Form):
    title = forms.CharField()
