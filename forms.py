from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Products


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'


class ProductMediaForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ["picture"]

class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)

