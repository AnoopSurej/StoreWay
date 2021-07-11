from django.urls import path, include
from . import views

urlpatterns = [
    path('cdashboard', views.customer_dashboard, name='customer-dashboard'),
    path('csearch', views.customer_search, name='customer-search'),
    path('cqueue', views.customer_queue, name='customer-queue'),
    path('shopdummy', views.shop_dummy, name='shop-dummy'),
    path('qrcode', views.qrcode_gen, name='qr-code-gen'),
    path('confirmalert', views.confirm_alert, name='confirm-alert'),
    path('shopitems',views.shop_items, name='shop_items'),
    path('orderhistory',views.order_history, name='order-history'),
    path('listaddress',views.list_address, name='list-address'),
    path('addaddress',views.add_address, name='add-address'),
]
