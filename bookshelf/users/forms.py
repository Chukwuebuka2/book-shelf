from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


# create forms here
class LoginForm(forms.Form):
    """User login form """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class UserSignupForm(UserCreationForm):
    """ User Signup form """
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label ="Password Confirmation", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username' , 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise ValidationError("Please confirm your password")

        if password1 != password2:
            raise ValidationError("Please check, passwords must match")

        return password2