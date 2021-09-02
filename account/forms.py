from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from imagekit_cropper.widgets import ImageCropWidget

from account.models import Account


class AccountForm(forms.ModelForm):
   
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
   
    class Meta:
        model = Account
        fields = ('email', 'password')
        
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Невірний логін або пароль")
