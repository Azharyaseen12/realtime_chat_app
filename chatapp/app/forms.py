from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2','profile_image')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # Add Bootstrap classes and custom styles to form fields
    #     self.fields['username'].widget.attrs.update({'class': 'form-control', 'style': 'border: 1px solid black; width: 300px; height: 25px;  padding: 6px 12px; box-sizing: border-box;'})
    #     self.fields['email'].widget.attrs.update({'class': 'form-control', 'style': 'border: 1px solid black; width: 300px; height: 25px; padding: 6px 12px; box-sizing: border-box;'})
    #     self.fields['password1'].widget.attrs.update({'class': 'form-control', 'style': 'border: 1px solid black; width: 300px; height: 25px; padding: 6px 12px; box-sizing: border-box;'})
    #     self.fields['password2'].widget.attrs.update({'class': 'form-control', 'style': 'border: 1px solid black; width: 300px; height: 25px; padding: 6px 12px; box-sizing: border-box;'})


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       