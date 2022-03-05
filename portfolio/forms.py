from django import forms

class ContactMe(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : "name",
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'placeholder': 'your mail',
    }))
    subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'subject',
    }))
    messages = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'message '
    }))