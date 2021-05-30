from django.shortcuts import render
# from shopkeeper.models import Shops
# from shopkeeper.forms import ShopDetailRegistrationForm

# def shopkeeper_register_next(request):
# 	owner_email = request.session.get('skemail')
# 	context = {}
# 	if request.POST:
# 		form = ShopDetailRegistrationForm(request.POST)
# 		if form.is_valid():
# 			data = request.POST.copy()
# 			data['owner_email'] = owner_email
# 			obj = Shops(data)
# 			obj.save()
# 			return redirect('storeapp-index')
# 		context['shop_detail_register_form'] = form

# 	else:
# 		form = CustomerRegistrationForm()
# 		context['shop_detail_register_form'] = form
# 	return render(request, "users/shopkeeper_register_next.html", context)