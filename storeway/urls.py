"""storeway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from storeapp import views as storeapp_views
from customer import views as customer_views
from shopkeeper import views as shopkeeper_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cregister/', user_views.customer_register, name='customer-register'),
    path('clogin/', user_views.customer_login, name='customer-login'),
    path('sregister/', user_views.shopkeeper_register, name='shopkeeper-register'),
    path('skregnext/', user_views.shopkeeper_register_next, name='shopkeeper-register-next'),
    path('slogin/', user_views.shopkeeper_login, name='shopkeeper-login'),
    path('clogout/', user_views.customer_logout, name='customer-logout'),
    path('', include('storeapp.urls')),
    path('', include('customer.urls')),
    # path('', include('shopkeeper.urls')),
]
