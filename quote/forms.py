from django import forms
from .models import Quote, Item

# class QuoteForm(forms.Form):
#     text = forms.CharField()

class NameForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["quote_name", "status",]
        labels = {"quote_name": "Project Name", "status": "status"}


class AddItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["species", "length",]
        labels = {"species": "X", "length": "Y",}






        # fields = ["species", "length", "width", "thickness", "quantity", "deadline", "quarter_sawn", "grade", "comments",]
        # labels = {"species": "Wood Species", "length": "Length", "width": "Width", "thickness": "Thickness", 
        #           "quantity": "Quantity", "deadline": "Deadline date", "quarter_sawn": "Quarter-Sawn", "grade": "Wood Grade",
        #           "comments": "Comments/ Instructions"}
