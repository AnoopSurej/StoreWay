from django.shortcuts import render, redirect
from users.forms import CustomerRegistrationForm, CustomerLoginForm, ShopkeeperLoginForm, ShopkeeperRegistrationForm, ShopDetailRegistrationForm
from django.contrib.auth import authenticate, login, logout
from shopkeeper.models import Shops


def customer_register(request):
	context = {}
	if request.POST:
		form = CustomerRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('storeapp-index')
		context['customer_register_form'] = form

	else:
		form = CustomerRegistrationForm()
		context['customer_register_form'] = form
	return render(request, "users/customer_register.html", context)

def customer_login(request):
	context = {}
	if request.POST:
		form = CustomerLoginForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(request, email=email, password=password)

			if user is not None:
				login(request, user)
				return redirect("customer-dashboard")
	else:
		form = CustomerLoginForm()
		context["customer_login_form"] = form

	return render(request, "users/customer_login.html", context)

def shopkeeper_register(request):
	context = {}
	if request.POST:
		form = ShopkeeperRegistrationForm(request.POST)
		if form.is_valid():
			sk = form.save()
			request.session['shopkeeper_email'] = sk.email
			return redirect('shopkeeper-register-next')
		context['shopkeeper_register_form'] = form

	else:
		form = ShopkeeperRegistrationForm()
		context['shopkeeper_register_form'] = form
	return render(request, "users/shopkeeper_register.html", context)

def shopkeeper_login(request):
	context = {}
	if request.POST:
		form = ShopkeeperLoginForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(request, email=email, password=password)

			if user is not None:
				login(request, user)
				return redirect("customer-dashboard")
	else:
		form = ShopkeeperLoginForm()
		context["shopkeeper_login_form"] = form

	return render(request, "users/shopkeeper_login.html", context)

def shopkeeper_register_next(request):
	shopkeeper_email = request.session.get('shopkeeper_email')
	context = {}
	if request.POST:
		form = ShopDetailRegistrationForm(request.POST)
		if form.is_valid():
			shop_name = request.POST.get('shop_name')
			shop_type = request.POST.get('shop_type')
			address = request.POST.get('address')
			district = request.POST.get('district')
			localbody = request.POST.get('localbody')
			wardnum = request.POST.get('wardnum')
			opening_time = request.POST.get('opening_time')
			closing_time = request.POST.get('closing_time')
			q_slot_time = request.POST.get('q_slot_time')
			q_slot_capacity = request.POST.get('q_slot_capacity')
			description = request.POST.get('description')
			obj = Shops(shopkeeper_email=shopkeeper_email, shop_name=shop_name, shop_type=shop_type, address=address, district = district, localbody = localbody, wardnum = wardnum, opening_time = opening_time, closing_time= closing_time, q_slot_time=q_slot_time,q_slot_capacity=q_slot_capacity, description=description)
			obj.save()
			return redirect('storeapp-index')
		context['shop_detail_register_form'] = form

	else:
		form = ShopDetailRegistrationForm()
		context['shop_detail_register_form'] = form
	return render(request, "users/shopkeeper_register_next.html", context)

def customer_dashboard(request):
	return render(request, "users/customer_dashboard.html")

def customer_logout(request):
	logout(request)
	return redirect('customer-register')

