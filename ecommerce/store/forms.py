from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
class NewsletterForm(forms.Form):
  email=forms.EmailField()




User = get_user_model()

class CustomRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text='Required. Enter your first name.')
    last_name = forms.CharField(max_length=50, required=True, help_text='Required. Enter your last name.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
