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
            'title': widgets.TextInput(attrs={
                'class': 'form-control',
                'id': 'title-input',
                'placeholder': 'Enter a project title'
            }),
            'comments': widgets.Textarea(attrs={
                'class': 'form-control',
                'id': 'comments-input',
                'placeholder': 'Leave us some comments'
            }),
            'deadline': widgets.DateInput(attrs={
                'type': 'date',
                'id': 'deadline-date',
                'class': 'form-control',
                'placeholder': 'Deadline'  
            }),
            'species': widgets.Select(attrs={
                'id': 'species-input',
                'class': 'form-control',
                'placeholder': 'Select Species'
            }),
            'width': TextInput(attrs={
                'type': "number",
                'min': '10',
                'max': '40',
                'id': 'width-input',
                'class': 'form-control',
                'placeholder': 'Enter width (10-40cm)'
            }),
            'thickness': TextInput(attrs={
                'type': "number",
                'min': '5',
                'max': '30',
                'id': 'depth-input',
                'class': 'form-control',
                'placeholder': 'Enter depth (5-30cm)'
                
            }),
            'length': widgets.Select(attrs={
                'id': 'length-input',
                'class': 'form-control',
                'placeholder': 'Select Length (cm)'
            }),
            'quarter_sawn': widgets.CheckboxInput(attrs={
                'id': 'quarter-input',
                'class': 'form-check-input',
            }),
            'grade': widgets.Select(attrs={
                'id': 'grade-input',
                'class': 'form-control',
                'placeholder': 'Select wood grade'
            }),
            'quantity': TextInput(attrs={
                'type': "number",
                'min': '1',
                'max': '40',
                'id': 'quantity-input',
                'class': 'form-control',
                'placeholder': 'Enter number of items'
                
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


