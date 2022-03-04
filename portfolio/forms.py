from django import forms

class ContactMe(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.CharField()
    subject = forms.CharField(max_length=100)
    messages = forms.CharField(widget=forms.Textarea)
