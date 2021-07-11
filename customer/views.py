from django.shortcuts import render
from shopkeeper.models import Shops
from users.models import StoreWayUser
from customer.models import CustomerQueue, CovidAlert, DeliveryAddress, OrderHistory
from shopkeeper.models import ShopRegistry
from shopkeeper.models import ContainmentZone,ShopItems
from io import BytesIO
from datetime import date,datetime, timedelta
from .forms import DeliveryAddressForm
import qrcode
import qrcode.image.svg

def customer_dashboard(request):
    current_user = request.user
    context={}
    context['user']=current_user
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
    searchterm = request.POST.get('searchterm')
    context = {}
    print(searchterm)
    if(searchterm=="" or searchterm is None):
        context = {'shops':Shops.objects.all()}
    else:
        list_of_ids = []
        id_shoptype = Shops.objects.filter(shop_type__icontains=searchterm)
        id_shopname = Shops.objects.filter(shop_name__icontains=searchterm)
        id_district = Shops.objects.filter(district__icontains=searchterm)
        id_localbody = Shops.objects.filter(localbody__icontains=searchterm)
        for query in id_shopname:
            list_of_ids.append(query.shopkeeper_email)
        for query in id_district:
            list_of_ids.append(query.shopkeeper_email)
        for query in id_localbody:
            list_of_ids.append(query.shopkeeper_email)
        for query in id_shoptype:
            list_of_ids.append(query.shopkeeper_email)
        list_of_ids = list(set(list_of_ids))
        entries = Shops.objects.filter(shopkeeper_email__in=list_of_ids)
        context['shops']=entries


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

        q_slot_time = shop.q_slot_time

        q_slot_capacity = shop.q_slot_capacity

        open_datetime = datetime(2000,1,1,hour=opening_time.hour,minute=opening_time.minute)
        close_datetime = datetime(2000,1,1,hour=closing_time.hour,minute=closing_time.minute)

        tdelta = timedelta(minutes=q_slot_time)

        temp = open_datetime

        while(temp<close_datetime):
            slots.append(temp)
            temp = temp + tdelta
            

        slot_times = [i.time() for i in slots]

        temp = slot_times

        for i in temp:
            if(CustomerQueue.objects.filter(shopkeeper_email = shopemail, queueTimeSlot = i).count()>=q_slot_capacity):
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

def shop_items(request):
    current_customer = request.user
    customer_email = current_customer.email
    customerFirstName = current_customer.first_name
    customerLastName = current_customer.last_name
    if request.method=='GET':
        shopemail = request.GET.get('shopemail')
        print(shopemail)
        shops=ShopItems.objects.filter(shopkeeper_email__contains=shopemail)
    if request.method=='POST':
        #form=OrderHistoryForm()
        shopemail = request.POST.get('shopkeeper_email')
        item_name=request.POST.get('item_name')
        item_price=request.POST.get('item_price')
        item_quantity=request.POST.get('item_quantity')
        if int(item_quantity)==1:
            obj=ShopItems.objects.filter(shopkeeper_email=shopemail, item_name=item_name)
            print(obj)
            obj.delete()
        else:
            item_quantity=int(item_quantity)-1
            ShopItems.objects.filter(shopkeeper_email=shopemail, item_name=item_name).update(item_quantity=item_quantity)
        shop = Shops.objects.get(shopkeeper_email=shopemail)
        shopname = shop.shop_name
        tday = datetime.now()
        tday_clean = datetime(tday.year,tday.month,tday.day,0,0)
        obj = OrderHistory(customerEmail=customer_email, customerFirstName=customerFirstName, customerLastName=customerLastName, shopkeeper_email=shopemail, shop_name=shopname, item_name=item_name, item_price=item_price, currentdate=tday_clean)
        obj.save()
        
        shops=ShopItems.objects.filter(shopkeeper_email__contains=shopemail)
        #return render(request,"customer/shop_items.html", {'shops':shops})

    return render(request,"customer/shop_items.html", {'shops':shops})


def order_history(request):
    
    current_customer = request.user
    customer_email = current_customer.email
    entries=OrderHistory.objects.filter(customerEmail=customer_email )
    print(entries)
    return render(request,"customer/orderhistory.html", {'entries':entries})

def list_address(request):
    if request.method=='GET':
        current_customer = request.user
        customer_email = current_customer.email
        entries=DeliveryAddress.objects.filter(customerEmail=customer_email ).count()
        print(entries)
        if entries==0:
            return render(request,"customer/list_address.html",{'entries':entries})
        else:
            addr=DeliveryAddress.objects.filter(customerEmail=customer_email )
            return render(request,"customer/list_address.html",{'entries':entries,'addr':addr})
   # if request.method=='POST':
    #    entries=request.POST.get('count')
        #return render(request,"customer/add_address.html", {'entries':entries})

def add_address(request):
        form=DeliveryAddressForm()
        current_customer = request.user
        customer_email = current_customer.email
        entries=DeliveryAddress.objects.filter(customerEmail=customer_email ).count()
        print(entries)
        if entries==0: 
            if request.method=="POST":
                form=DeliveryAddressForm(request.POST)
                if form.is_valid():
                    current_customer = request.user
                    customer_email = current_customer.email
                    delivery_address=request.POST.get('delivery_address')
                    delivery_pin=request.POST.get('delivery_pin')
                    delivery_district=request.POST.get('delivery_district')
                    obj = DeliveryAddress(customerEmail=customer_email, delivery_address=delivery_address,delivery_pin =delivery_pin, delivery_district=delivery_district)
                    obj.save()
                    return render(request,"customer/customer_dashboard.html")
                
            else:
                return render(request,'customer/add_address.html', {'form':form})
    
        else:
            if request.method=="POST":
                form=DeliveryAddressForm(request.POST)
                if form.is_valid():
                    current_customer = request.user
                    customer_email = current_customer.email
                    delivery_address=request.POST.get('delivery_address')
                    delivery_pin=request.POST.get('delivery_pin')
                    delivery_district=request.POST.get('delivery_district')
                    DeliveryAddress.objects.filter(customerEmail=customer_email).update(delivery_address=delivery_address)
                    delivery_pin=int(delivery_pin)
                    DeliveryAddress.objects.filter(customerEmail=customer_email).update(delivery_pin=delivery_pin)
                    DeliveryAddress.objects.filter(customerEmail=customer_email).update(delivery_district=delivery_district)
                    return render(request,"customer/customer_dashboard.html")
                else:
                    form=DeliveryAddressForm()
                    return render(request,'customer/add_address.html', {'form':form})
            else:
                form=DeliveryAddressForm()
                return render(request,'customer/add_address.html', {'form':form})
        return render(request,'customer/add_address.html', {'form':form})
	    