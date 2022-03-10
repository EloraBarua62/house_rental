from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from .models import User, HouseDetails, HouseRate, ShowMap, AdminHouse


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phoneno']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'userid':forms.TextInput(attrs={'class':'form-control'}),
            'phoneno': forms.TextInput(attrs={'class': 'form-control'}),
        }


class HouseInfoForm(forms.ModelForm):
    class Meta:
        model = HouseDetails
        fields = "__all__"
        # fields = ['house_id', 'size', 'total_room', 'bed', 'parking_lot', 'floor']
        # widgets = {
        #     'house_id': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'size': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'total_room': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'bed': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'parking_lot': forms.TextInput(attrs={'class': 'form-control'}),
        #     'floor': forms.TextInput(attrs={'class': 'form-control'})
        # }


class AdminHouseForm(forms.ModelForm):
    class Meta:
        model = AdminHouse
        fields = "__all__"


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)


class HouseRateForm(forms.ModelForm):
    class Meta:
        model = HouseRate
        fields = "__all__"


class ShowMapForm(forms.ModelForm):
    address = forms.CharField(label='')

    class Meta:
        model = ShowMap
        fields = ['address', ]
