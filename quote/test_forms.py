from django.test import TestCase
from .forms import QuoteForm

class TestQuoteForm(TestCase):

    def test_title_name_is_required(self):
        form = QuoteForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_species1(self):
        form = QuoteForm({'species': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('species', form.errors.keys())
        self.assertEqual(form.errors['species'][0], 'This field is required.')

    def test_deadline(self):
        form = QuoteForm({'deadline': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('deadline', form.errors.keys())
        self.assertEqual(form.errors['deadline'][0], 'This field is required.')

    def test_comments(self):
        form = QuoteForm({'comments': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('comments', form.errors.keys())
        self.assertEqual(form.errors['comments'][0], 'This field is required.')

    def test_length(self):
        form = QuoteForm({'length': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('length', form.errors.keys())
        self.assertEqual(form.errors['length'][0], 'This field is required.')

    def test_width(self):
        form = QuoteForm({'width': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('width', form.errors.keys())
        self.assertEqual(form.errors['width'][0], 'This field is required.')

    def test_width(self):
        form = QuoteForm({'width': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('width', form.errors.keys())
        self.assertEqual(form.errors['width'][0], 'This field is required.')

    def test_thickness(self):
        form = QuoteForm({'thickness': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('thickness', form.errors.keys())
        self.assertEqual(form.errors['thickness'][0], 'This field is required.')

    def test_quantity(self):
        form = QuoteForm({'quantity': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('quantity', form.errors.keys())
        self.assertEqual(form.errors['quantity'][0], 'This field is required.')

    def test_grade(self):
        form = QuoteForm({'grade': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('grade', form.errors.keys())
        self.assertEqual(form.errors['grade'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = QuoteForm()
        self.assertEqual(form.Meta.fields, ['title', 'deadline', 'comments',
                                            'species', 'length', 'width',
                                            'thickness', 'quantity',
                                            'quarter_sawn', 'grade'])
