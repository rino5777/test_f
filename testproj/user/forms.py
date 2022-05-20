from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from user.models import Profile
from django.forms import ModelForm




class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):   # игнорирование стандартных стилей 
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({ 'class': 'form-control', 'placeholder': 'Password' , 'rows': 1, })
        self.fields['password2'].widget.attrs.update({ 'class': 'form-control', 'placeholder': 'Confirm Password' , 'rows': 1, })
        self.fields['email'].widget.attrs.update({ 'class': 'form-control', 'placeholder': 'E-mail Address' , 'rows': 1, })
        self.fields['username'].widget.attrs.update({ 'class': 'form-control', 'placeholder': 'Username' , 'rows': 1, })
        self.fields['first_name'].widget.attrs.update({ 'class': 'form-control', 'placeholder': 'Username' , 'rows': 1, })
        self.fields['last_name'].widget.attrs.update({ 'class': 'form-control', 'placeholder': 'Username' , 'rows': 1, })

    class Meta:
        model = User
        fields = [ 'username', 'first_name',  'email',  'password1', 'last_name']





class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [ 'name', 'surname', 'patronymic' ]






