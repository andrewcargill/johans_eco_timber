from django import forms
from django.forms import TextInput
from .models import Quote, Item



# class QuoteForm(forms.Form):
#     text = forms.CharField()

class NameForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["quote_name", "status",]
        labels = {"quote_name": "Project Name", "status": "status"}


SPECIES = [('Pine', 'Pine'), ('Birch', 'Birch'), ('Spruce', 'Spruce')]

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





# class AddItem(forms.ModelForm):
#     class Meta:
#         model = Item
#         fields = ["species", "length",]
#         labels = {"species": "X", "length": "Y",}






        # fields = ["species", "length", "width", "thickness", "quantity", "deadline", "quarter_sawn", "grade", "comments",]
        # labels = {"species": "Wood Species", "length": "Length", "width": "Width", "thickness": "Thickness", 
        #           "quantity": "Quantity", "deadline": "Deadline date", "quarter_sawn": "Quarter-Sawn", "grade": "Wood Grade",
        #           "comments": "Comments/ Instructions"}
