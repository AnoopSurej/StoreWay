from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from users.models import StoreWayUser
from shopkeeper.models import Shops

class CustomerRegistrationForm(UserCreationForm):
	user_type = forms.CharField(widget=forms.HiddenInput(),initial='CUSTOMER' )
	class Meta:
		model = StoreWayUser
		fields = ('email','first_name','last_name','phone','password1','password2','user_type')
		widgets = {'user_type': forms.HiddenInput()}


class CustomerLoginForm(forms.ModelForm):
	password = forms.CharField(label = "Password", widget = forms.PasswordInput)

	class Meta:
		model = StoreWayUser
		fields = ['email','password']

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']

			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid credentials")

class ShopkeeperRegistrationForm(UserCreationForm):
	user_type = forms.CharField(widget=forms.HiddenInput(),initial='SHOPKEEPER' )
	class Meta:
		model = StoreWayUser
		fields = ('email','first_name','last_name','phone','password1','password2','user_type')
		widgets = {'user_type': forms.HiddenInput()}


class ShopkeeperLoginForm(forms.ModelForm):
	password = forms.CharField(label = "Password", widget = forms.PasswordInput)

	class Meta:
		model = StoreWayUser
		fields = ['email','password']

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']

			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid credentials")

class ShopDetailRegistrationForm(forms.ModelForm):
	class Meta:
		model = Shops
		fields = ('shop_name','shop_type','address','district','localbody','wardnum','opening_time','closing_time','q_slot_time','q_slot_capacity','description')




