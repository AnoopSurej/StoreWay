from django.urls import path, include
from . import views

urlpatterns = [
    path('sdashboard', views.shopkeeper_dashboard, name='shopkeeper-dashboard'),
    path('qrscan', views.qr_scan, name='qr-scan'),
    path('shopregistry', views.shopregistry, name='shop-registry'),
    path('covidalert', views.covid_alert, name='covid-alert'),
    path('covidalertnotif', views.covid_alert_notif, name='covid-alert-notif'),
    path('additem', views.add_item, name='add_item'),
    path('listitems', views.list_items, name='list_items'),
    path('order_history',views.order_history, name='order-history'),

]