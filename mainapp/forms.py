from django import forms

class Registration(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField()
    address = forms.CharField()
