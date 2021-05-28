from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserForm(UserCreationForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if self.Meta.model.objects.filter(email=email).exists():
            raise forms.ValidationError('Looks like email already exists')
        return email

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')   
        
       
        
    

