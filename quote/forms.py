from django import forms
from django.forms import TextInput
from .models import Quote, Item, QuoteData

#from original plan
#quote database view to add project title
class NameForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["quote_name", "status",]
        labels = {"quote_name": "Project Name", "status": "status"}


SPECIES = [('Pine', 'Pine'), ('Birch', 'Birch'), ('Spruce', 'Spruce')]

#from original plan
#Item view
class AddItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['quote_id', 'deadline', 'comments', 'species', 'length',
                  'width', 'thickness', 'quantity', 'quarter_sawn', 'grade']
        widgets = {
            'deadline': TextInput(attrs={
                'type': "date",
            }),
            'width': TextInput(attrs={
                'type': "number",
                'min': '10',
                'max': '40',
                'placeholder': 'Tell me about what you need and any specific instructions'
            }),
            'thickness': TextInput(attrs={
                'type': "number",
                'min': '5',
                'max': '40',
                'placeholder': 'Tell me about what you need and any specific instructions'
            }),
            'quantity': TextInput(attrs={
                'type': "number",
                'min': '1',
                'max': '40',
                'placeholder': 'Tell me about what you need and any specific instructions'
            }),
        }

#Single page solution
class QuoteForm(forms.ModelForm):
    class Meta:
        model = QuoteData
        fields = ['title', 'deadline', 'comments', 'species', 'length_new',
                  'width', 'thickness', 'quantity', 'quarter_sawn', 'grade']
        widgets = {
            'deadline': TextInput(attrs={
                'type': "date",
            }),
            'width': TextInput(attrs={
                'type': "number",
                'min': '10',
                'max': '40',
                'placeholder': 'Tell me about what you need and any specific instructions'
            }),
            'thickness': TextInput(attrs={
                'type': "number",
                'min': '5',
                'max': '40',
                'placeholder': 'Tell me about what you need and any specific instructions'
            }),
            'quantity': TextInput(attrs={
                'type': "number",
                'min': '1',
                'max': '40',
                'placeholder': 'Tell me about what you need and any specific instructions'
            }),
        }


