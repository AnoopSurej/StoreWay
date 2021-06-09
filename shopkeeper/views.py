from django.shortcuts import render
from .models import ShopRegistry
from .models import Shops
from customer.models import CovidAlert
from users.models import StoreWayUser
import datetime
import cv2

def shopkeeper_dashboard(request):
	return render(request, 'shopkeeper/shopkeeper_dashboard.html')

def qr_scan(request):
	context = {}

	current_shopkeeper = request.user
	current_shopkeeper_email = current_shopkeeper.email

	shop = Shops.objects.get(shopkeeper_email=current_shopkeeper_email)

	cap = cv2.VideoCapture(0)
	detector = cv2.QRCodeDetector()
	details = None
	print("here A")
	while details is None:
	    _, img = cap.read()
	    data, bbox, _ = detector.detectAndDecode(img)
	    print("Here B")
	    if bbox is not None:
	        for i in range(len(bbox)):
	            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
	            print("Here C")
	        if data:
	            details = data.split(";")
	            semail = details[0]
	            cfirstname = details[2]
	            clastname = details[3]
	            cphone = details[4]
	            sname = details[5]
	            qslot = details[6]
	            print("Here D")
	            print(semail)
	            print(current_shopkeeper_email)
	            tday = datetime.datetime.now()
	            tday_clean = datetime.datetime(tday.year,tday.month,tday.day,0,0)
	            if(semail==current_shopkeeper_email):
	            	print("here1")
	            	if(ShopRegistry.objects.filter(shopkeeper_email=semail,customerFirstName=cfirstname,customerLastName=clastname,customerPhone=cphone,queueTimeSlot=qslot,dateEntry=tday_clean).count()<1):
	            		print("here2")
	            		obj = ShopRegistry(shopkeeper_email=semail,customerFirstName=cfirstname,customerLastName=clastname,customerPhone=cphone,queueTimeSlot=qslot,dateEntry=tday_clean)
	            		obj.save()
	            		context['status']="Scan Successful! Entry Added!"
	            	else:
	            		context['status']="Scan Successful! Entry Not Added As It Already Exists"
	            		print(tday_clean)
	            		print(type(tday_clean))
	            else:
	            	context['status'] = "Scan Successful! WRONG STORE"

	    cv2.imshow("img", img)
	    if details is not None:
	        break 
	    if cv2.waitKey(1) == ord("q"):
	        break
	cap.release()
	cv2.destroyAllWindows()

	return render(request,'shopkeeper/qr_scan.html',context)

def shopregistry(request):
	current_shopkeeper = request.user
	current_shopkeeper_email = current_shopkeeper.email

	entries = ShopRegistry.objects.filter(shopkeeper_email=current_shopkeeper_email)

	context = {
	'entries':entries
	}

	return render(request,'shopkeeper/shopregistry.html',context)

def covid_alert(request):
	current_shopkeeper = request.user
	current_shopkeeper_email = current_shopkeeper.email

	entries = ShopRegistry.objects.filter(shopkeeper_email=current_shopkeeper_email)

	context = {
	'entries':entries
	}

	return render(request,'shopkeeper/covid_alert.html',context)

def covid_alert_notif(request):
	slot = request.GET.get('timeslot')
	print(slot)
	date = request.GET.get('date')
	val = date.split("-")
	val_int = [int(i) for i in val]
	val_int = val_int[::-1]
	datetimeobj = datetime.datetime(val_int[0],val_int[1],val_int[2])
	shopkeeper = request.user
	semail = shopkeeper.email
	phone = request.GET.get('phone')

	if not slot:
		print("Error")
		return render(request,"shopkeeper/shopkeeper_dashboard.html")
	else:
		# customer = StoreWayUser.objects.get(phone=phone)
		# cemail = customer.email
		shop = Shops.objects.get(shopkeeper_email=semail)
		shopname = shop.shop_name

		user_test = ShopRegistry.objects.get(customerPhone=phone)

		print(user_test.queueTimeSlot)

		# obj = CovidAlert(customerEmail=cemail,shop_name=shopname, date=datetimeobj)

		# obj.save()

		# others = ShopRegistry.objects.filter(queueTimeSlot=slot).exclude(customerPhone=phone)

		# for i in others:
		# 	customer = StoreWayUser.objects.get(phone=i.customerPhone)
		# 	cemail = customer.email

		# 	obj = CovidAlert(customerEmail=cemail,shop_name=shopname,date=datetimeobj)

		# 	obj.save()

		covid = ShopRegistry.objects.filter(shopkeeper_email=semail,queueTimeSlot=slot,dateEntry=datetimeobj)

		print(covid)

		for i in covid:
			customer = StoreWayUser.objects.get(phone=i.customerPhone)
			cemail = customer.email

			print(cemail)

			obj = CovidAlert(customerEmail=cemail, shop_name=shopname, date = datetimeobj)

			obj.save()

		return render(request,"shopkeeper/shopkeeper_dashboard.html")