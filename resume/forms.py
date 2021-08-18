from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = "__all__"
    widgets = {
            'name': forms.TextInput(attrs={'class': 'w3-input'}),
            'email': forms.TextInput(attrs={'class': 'w3-input'}),
            'subject': forms.TextInput(attrs={'class': 'w3-input'}),
            'message': forms.Textarea(attrs={'class': 'w3-input'}),
        }