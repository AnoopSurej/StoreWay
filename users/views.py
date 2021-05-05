from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateCustomerUserForm

def customer_register(request):
	if request.method == 'POST':
		form = CreateCustomerUserForm(request.POST)
		if form.is_valid():
			#form.save()
			#username = form.cleaned_data.get('username')
			#messages.success(request, f'Account created for {username}!')
			return redirect('storeapp-index')
		else:
			messages.error(request, f'Error')

	else:
		form = CreateCustomerUserForm()
	return render(request, 'users/customer_register.html', {'form':form})
