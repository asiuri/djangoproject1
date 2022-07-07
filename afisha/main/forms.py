from django import forms
from django.core.exceptions import ValidationError

from main.models import Movie,Director
from django.contrib.auth.models import User



class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = 'tittle description year  category  directors  actors '.split()
        widgets = {
            'tittle': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ' Write  a name of the movie'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Fill in the description'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'When  is the movie directed'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'

            }),
            'directors': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Who is the director of this movie'
            }),
            'actors': forms.TextInput(attrs={
                'class': 'form-control'

            }),

        }


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = 'name '.split()
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ' Write  a name of the director'
            }),

        }
class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))


    def clean_username(self):
        username = self.cleaned_data['username']
        users = User.objects.filter(username=username)
        if users:
            raise ValidationError('User already exists')
        return username


    def clean_email(self):
        email = self.cleaned_data['email']
        users = User.objects.filter(email=email)
        if users:
            raise ValidationError('Email mast be provided')
        return email


    def clean_password1(self):
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password']
        if password != password1:
            raise ValidationError('Passwords do not match')
        return password

    def save(self):
        """Create User"""
        username=self.cleaned_data['username']
        email=self.cleaned_data['email']
        password=self.cleaned_data['password']
        user=User.objects.create_user(username=username,email=email,password=password)
        return user

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
