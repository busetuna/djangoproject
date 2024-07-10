from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from matplotlib import widgets
from django import forms
from django.forms import widgets
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    def __init__(self , *args , **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs = { "class" : "form-control"})
        self.fields["password"].widget = widgets.PasswordInput(attrs = { "class" : "form-control"})



class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})