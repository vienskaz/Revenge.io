from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewsletterForm(forms.Form):
  email=forms.EmailField()

  
class CustomRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text=None,widget=forms.TextInput(attrs={'class': 'registerinput'}))
    last_name = forms.CharField(max_length=50, required=True, help_text=None,widget=forms.TextInput(attrs={'class': 'registerinput'}))    
    email = forms.EmailField(required=True, help_text=None,widget=forms.TextInput(attrs={'class': 'registerinput'})) 

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1']

    def __init__(self, *args, **kwargs):
        super(CustomRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['email'].label = "Email"
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
       


        self.fields['username'].help_text = None
        self.fields['email'].help_text = None
        self.fields['first_name'].help_text = None
        self.fields['last_name'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

        self.fields['username'].widget.attrs['class'] = 'registerinput'
        self.fields['password1'].widget.attrs['class'] = 'registerinput'
        self.fields['password2'].widget.attrs['class'] = 'registerinput'


