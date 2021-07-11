from django import forms
from django.forms import ModelForm
from shopkeeper.models import ShopItems

class AddItemForm(ModelForm):
    class Meta:
        model = ShopItems
        fields = ('item_name','item_price','item_quantity','item_description')  
        labels=  {
            'item_name':'  ',
            'item_price':'  ',
            'item_quantity':'  ',
            'item_description':'  ',
        }
        widgets = {
            'item_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the item name '}),
            'item_price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the item price'}),
            'item_quantity':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Enter the quantity'}),
            'item_description':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the description'}),
        }