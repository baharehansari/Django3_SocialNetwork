from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'bahar'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'bahar@gmail.com'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'confirm password'}))


    # email validation : cleaning a specific field attribute
    def clean_email(self):
        email = self.cleaned_data['email']
        # user= User.objects.filter(email=email): بهینه نیست
        user = User.objects.filter(email=email).exists() # it is a query set # answer is True or False
        if user:
            raise ValidationError('this email is already exists.')
        return email

    # password validation : cleaning and validating fields that depend on each other
    def Clean(self):
        cd = super().clean()
        p1 = cd.get('password1')
        p2 = cd.get('password2')
        if p1 and p2 and p1 != p2:
            raise ValidationError('passwords did not match!')


class UserLoginForm(forms.Form):
    username = forms.CharField(label='username/email',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'bahar or bahar@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))


