from django import forms
from django.forms import TextInput, widgets
from .models import QuoteData
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



#Single page solution

class QuoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuoteForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = QuoteData
        fields = ['title', 'deadline', 'comments', 'species', 'length',
                  'width', 'thickness', 'quantity', 'quarter_sawn', 'grade']
        widgets = {
            'deadline': widgets.DateInput(attrs={'type': 'date'}),
            'width': TextInput(attrs={
                'type': "number",
                'min': '10',
                'max': '40',
                
            }),
            'thickness': TextInput(attrs={
                'type': "number",
                'min': '5',
                'max': '40',
                
            }),
            'quantity': TextInput(attrs={
                'type': "number",
                'min': '1',
                'max': '40',
                
            }),
        }

# class QuoteForm(forms.ModelForm):
#     class Meta:
#         model = QuoteData
#         fields = ['title', 'deadline', 'comments', 'species', 'length',
#                   'width', 'thickness', 'quantity', 'quarter_sawn', 'grade']
#         widgets = {
#             'deadline': widgets.DateInput(attrs={'type': 'date'}),
#             'width': TextInput(attrs={
#                 'type': "number",
#                 'min': '10',
#                 'max': '40',
#                 'placeholder': 'Tell me about what you need and any specific instructions'
#             }),
#             'thickness': TextInput(attrs={
#                 'type': "number",
#                 'min': '5',
#                 'max': '40',
#                 'placeholder': 'Tell me about what you need and any specific instructions'
#             }),
#             'quantity': TextInput(attrs={
#                 'type': "number",
#                 'min': '1',
#                 'max': '40',
#                 'placeholder': 'Tell me about what you need and any specific instructions'
#             }),
#         }


