from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, required=True, 
        widget=forms.TextInput(attrs={
            'placeholder': '*Email Address...',
            'class': 'form-control'
            }))
    subject = forms.CharField(max_length=250, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Subject..',
            'class': 'form-control'
            }))
    message = forms.CharField(max_length=1000, required=True, 
        widget=forms.Textarea(attrs={
            'placeholder': '*Message..',
            'class': 'form-control',
            'rows': 6,
            }))


    class Meta:
        model = Contact
        fields = ('email', 'subject', 'message',)

