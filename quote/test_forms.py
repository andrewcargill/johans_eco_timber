from django.test import TestCase
from .forms import QuoteForm

class TestQuoteForm(TestCase):

    def test_title_name_is_required(self):
        

