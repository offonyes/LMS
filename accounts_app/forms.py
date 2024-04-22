from django import forms
from accounts_app.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class LoginForm(forms.Form):
    username = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            validate_email(username)
        except ValidationError:
            raise ValidationError("Please enter a valid email address.")
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        return password

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    passport_number = forms.CharField(max_length=11)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'passport_number', 'email', 'password1', 'password2', )
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False  # Set is_active to False by default
        if commit:
            user.save()
        return user