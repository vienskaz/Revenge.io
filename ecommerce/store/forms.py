from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class NewsletterForm(forms.Form):
  email=forms.EmailField()






from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text='')
    last_name = forms.CharField(max_length=50, required=True, help_text='')    
    email = forms.EmailField(required=True, help_text='') 

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1']

    def __init__(self, *args, **kwargs):
        super(CustomRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['email'].label = "Email"
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
       
        # You can also set custom CSS classes for fields:
        self.fields['first_name'].widget.attrs['class'] = 'custom-class'
        self.fields['last_name'].widget.attrs['class'] = 'custom-class'
        self.fields['email'].widget.attrs['class'] = 'custom-class'
        self.fields['password1'].widget.attrs['class'] = 'custom-class'
        self.fields['password2'].widget.attrs['class'] = 'custom-class'
