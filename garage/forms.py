from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Логин',
        )
    email = forms.CharField(
        max_length=150,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    password1 = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Пароль',
    )
    password2 = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Подтвердите пароль',
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserAuthentication(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Логин',
        )

    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Пароль',
    )

    class Meta:
        model = User
        fields = ['username', 'password',]


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owners
        fields = [
            'first_name', 
            'patronymic', 
            'second_name',
            ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'}),
            'second_name': forms.TextInput(attrs={'class': 'form-control'}),
        }  


class ManufactForm(forms.ModelForm):
    class Meta:
        model = Manufacturers
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }


class CarModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CarModelForm, self).__init__(*args, **kwargs)
        self.fields['manufacturer'].empty_label = None

    class Meta:
        model = CarModels
        fields = [
            'manufacturer', 
            'title'
            ]
        widgets = {
            'title': forms.TextInput(attrs={'size': '40', 'class': 'form-control'}),
            'manufacturer': forms.Select(attrs={'class': 'form-control',})
        }


class MechanicsForm(forms.ModelForm):
    class Meta:
        model = Mechanics
        fields = [
            'second_name', 
            'first_name',
            'patronymic',
            'experience',
            ]
        widgets = {
            'second_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control'}),            
        }


class CarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields['owner'].empty_label = None
        self.fields['manufacturer'].empty_label = None
        self.fields['car_model'].empty_label = None
        self.fields['mechanic'].empty_label = None


    class Meta:
        model = Cars
        fields = [
            'owner',
            'manufacturer', 
            'car_model',
            'color',
            'gov_number',
            'year',
            'ser_sts',
            'num_sts',
            'scan_sts',
            'photo',
            'type_of_repair',            
            'date_of_issue',         
            'mechanic',
            ]
        widgets = {
            'owner': forms.Select(attrs={'class': 'form-control'}),
            'manufacturer': forms.Select(attrs={'class': 'form-control'}),
            'car_model': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'gov_number': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'ser_sts': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_sts': forms.NumberInput(attrs={'class': 'form-control'}),
            'scan_sts': forms.FileInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'type_of_repair': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'date_of_issue': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'mechanic': forms.Select(attrs={'class': 'form-control'}),
        }
        

    def clean_year(self):
        year = self.cleaned_data['year']
        if not 1970 < year < 2023:
            raise ValidationError('Введите корректный год выпуска')
        return year


class PriceForm(forms.ModelForm):
    class Meta:
        model = PriceList
        fields = [
            'type_of_repair',
            'price',
        ]
        widgets = {
            'type_of_repair': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }