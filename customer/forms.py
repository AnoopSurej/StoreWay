from django import forms
from django.forms import ModelForm
from customer.models import DeliveryAddress


class DeliveryAddressForm(ModelForm):
    class Meta:
        model = DeliveryAddress
        fields = ('delivery_address','delivery_pin','delivery_district')  
        labels=  {
            'delivery_address':'  ',
            'delivery_pin':'  ',
            'delivery_district':'  ',
        }
        widgets = {
            'delivery_address':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the Address'}),
            'delivery_pin':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the pincode'}),
            'delivery_district':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the district'}),
        }