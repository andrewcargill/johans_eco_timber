from django import forms
from .models import Quote

# class QuoteForm(forms.Form):
#     text = forms.CharField()

class NameForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["quote_name", "status",]
        labels = {"quote_name": "Project Name", "status": "status"}
