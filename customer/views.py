from django.shortcuts import render
from shopkeeper.models import Shops
from users.models import StoreWayUser
from customer.models import CustomerQueue, CovidAlert
from shopkeeper.models import ShopRegistry
from shopkeeper.models import ContainmentZone
from io import BytesIO
from datetime import datetime, timedelta
import qrcode
import qrcode.image.svg

def customer_dashboard(request):
    current_user = request.user
    context={}
    covid = False

    if(CovidAlert.objects.filter(customerEmail=current_user.email,is_read=False).count()>=1):
        covid = True
        obj = CovidAlert.objects.filter(customerEmail=current_user.email,is_read=False)[0]
        shopname = obj.shop_name
        time = obj.time
        date = obj.date
        context['shopname'] = shopname
        context['time'] = time
        context['date'] = date
    

    context['covid']=covid

    return render(request,'customer/customer_dashboard.html',context)
	# context = {
	# 'shops':Shops.objects.all()
	# }

	# return render(request, 'customer/temp.html',context)

def customer_search(request):
    current_user = request.user
    context = {'shops':Shops.objects.all()}

    return render(request,'customer/customer_search.html',context)

def shop_dummy(request):
    current_user = request.user
    if request.method=='GET':
        shopname = request.GET.get('shopname')
        if not shopname:
            return render(request, 'customer-dashboard')
        else:
            shop = Shops.objects.get(shop_name = shopname)
            context = {
            'shop':shop
            }
        slots = []

        status = ""

        if(ContainmentZone.objects.filter(district=shop.district,localbody=shop.localbody,wardnum=shop.wardnum).count()>=1):
            status = "CONTAINMENT"

        context['status']=status

        shopemail = shop.shopkeeper_email

        shopKeeper = StoreWayUser.objects.get(email=shopemail)

        context['sphone']=shopKeeper.phone

        opening_time = shop.opening_time

        closing_time = shop.closing_time

        open_datetime = datetime(2000,1,1,hour=opening_time.hour,minute=opening_time.minute)
        close_datetime = datetime(2000,1,1,hour=closing_time.hour,minute=closing_time.minute)

        tdelta = timedelta(minutes=15)

        temp = open_datetime

        while(temp<close_datetime):
            slots.append(temp)
            temp = temp + tdelta
            

        slot_times = [i.time() for i in slots]

        temp = slot_times

        for i in temp:
            if(CustomerQueue.objects.filter(shopkeeper_email = shopemail, queueTimeSlot = i).count()>=5):
                slot_times.remove(i)

        slot_times_formatted = [i.strftime("%H:%M") for i in slot_times]

        context['slot_times_formatted'] = slot_times_formatted

        print(slot_times_formatted)
    return render(request,'customer/shopdummy.html',context)

def qrcode_gen(request):
    context = {}
    current_user = request.user
    if request.method=='GET':
        shopemail = request.GET.get('shopemail')
        slot_time  = request.GET['slot']
        print(shopemail)
        if not shopemail:
            return render(request,'customer-dashboard')
        else:
            customerFirstName = current_user.first_name
            customerLastName = current_user.last_name
            customerEmail = current_user.email
            customerPhone = current_user.phone
            shop = Shops.objects.get(shopkeeper_email = shopemail)
            shopkeeper_email = shop.shopkeeper_email
            shopname = shop.shop_name
            queueSlotTime = slot_time

            #QR Code Generation

            data = "{shopkeeper_email};{shopname};{customerFirstName};{customerLastName};{customerPhone};{shopname};{queueSlotTime}".format( shopkeeper_email = shopkeeper_email, customerFirstName = customerFirstName, customerLastName = customerLastName, customerPhone = customerPhone, shopname = shopname, queueSlotTime = queueSlotTime )
            factory = qrcode.image.svg.SvgImage
            qr = qrcode.make(data, image_factory = factory, box_size = 25)

            stream = BytesIO()

            qr.save(stream)

            queue = CustomerQueue(customerEmail = customerEmail, shop_name = shopname, customerFirstName = customerFirstName, customerLastName = customerLastName, customerPhone = customerPhone, shopkeeper_email = shopkeeper_email, queueTimeSlot = queueSlotTime)

            queue.save()

            context['svg'] = stream.getvalue().decode

    return render(request,'customer/qr.html', context)

def customer_queue(request):
    current_user = request.user

    entries = CustomerQueue.objects.filter(customerEmail=current_user.email)

    context = {
    'entries':entries,
    }

    return render(request,"customer/customer_queue.html",context)

def confirm_alert(request):
    current_user = request.user
    shopname = request.GET.get('shopname')

    obj = CovidAlert.objects.filter(customerEmail=current_user.email,shop_name=shopname)

    obj.update(is_read=True)

    return render(request,"customer/customer_dashboard.html")