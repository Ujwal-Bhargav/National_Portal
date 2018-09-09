from django import forms
from  Nation_Portalapp.models import *
from django.contrib.auth import login,logout,authenticate,get_user_model

User=get_user_model()

class SignUpForm(forms.Form):
    first_name=forms.CharField(label='Enter your first name',max_length=300)
    last_name = forms.CharField(label='Enter your last name', max_length=100)
    username = forms.CharField(label='Enter your user name', max_length=100)
    password = forms.CharField(label='Enter password', max_length=100)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        if username and password:
            user=authenticate(username=username,password=password)
            if not  user:
                raise  forms.ValidationError("This user doesnot exist")
            if not user.check_password(password):
                raise   forms.ValidationError("Incorrect password")
        return super(LoginForm,self).clean(*args,**kwargs)

class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password'
        ]


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=[
            'issue',
            'complaint',
            'location',
            'image'
        ]

