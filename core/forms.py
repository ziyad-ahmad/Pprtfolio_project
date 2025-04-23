from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """Contact form for the portfolio website"""
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('name', css_class='rounded-lg'),
            Field('email', css_class='rounded-lg'),
            Field('subject', css_class='rounded-lg'),
            Field('message', css_class='rounded-lg'),
            Submit('submit', 'Send Message', css_class='btn-primary mt-4')
        )