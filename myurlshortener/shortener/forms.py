from django import forms

class Urlform(forms.Form):
    url = forms.URLField()
    custom = forms.CharField(max_length=100, required=False)

class Register(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=254)
    password = forms.CharField(max_length=128)
    confirm_password = forms.CharField(max_length=128)

class Login(forms.Form):
    username = forms.CharField(max_length=150)
    # email = forms.EmailField(max_length=254)
    password = forms.CharField(max_length=128)
