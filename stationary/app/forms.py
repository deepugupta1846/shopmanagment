from django import forms
from .models import *


class Additem(forms.ModelForm):
    class Meta:
        model = ShopManagment
        fields = ['Item_Name', 'Company', 'Type', 'Rate']
        widgets = {
            'Item_Name': forms.TextInput(attrs={'placeholder': 'Enter Item Name', 'class': 'form-control'}),
            'Company': forms.TextInput(attrs={'placeholder': 'Enter Item Company Name', 'class': 'form-control'}),
            'Type': forms.TextInput(attrs={'placeholder': 'Item Type', 'class': 'form-control'}),
            'Rate': forms.TextInput(attrs={'placeholder': 'Rate', 'class': 'form-control'}),
        }