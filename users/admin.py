from django.contrib import admin
from users.models import StoreWayUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class StoreWayUserAdmin(BaseUserAdmin):
	list_display = ['email','first_name', 'last_name', 'date_joined','last_login','user_type','is_admin', 'is_active']
	search_fields = ['email']
	readonly_fields = ['date_joined','last_login']
	filter_horizontal = []
	list_filter = ['last_login']
	fieldsets = []

	add_fieldsets = [
		(None, {
			'classes':('wide'),
			'fields':('email','first_name','last_name','phone','password1','password2')
			}


			)
	]

	ordering = ['email']

admin.site.register(StoreWayUser, StoreWayUserAdmin)
