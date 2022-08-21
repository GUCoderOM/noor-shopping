from django import forms
from shopping.models import User
from django.contrib.auth.models import User
from shopping.models import UserProfile


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=120,)
    email = forms.EmailField(max_length=120,)
    #age = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput())
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = User
        fields = ('username','email','password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('age','picture')
