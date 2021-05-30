from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class StoreWayUserManager(BaseUserManager):
	def create_user(self, email, first_name, last_name, phone, user_type, password=None):
		if not email:
			raise ValueError("Email is required")
		if not first_name:
			raise ValueError("First Name is required")
		if not last_name:
			raise ValueError("Last Name is required")
		if not phone:
			raise ValueError("Phone Number is required")

		user = self.model(
			email = self.normalize_email(email),
			first_name = first_name,
			last_name = last_name,
			phone = phone,
			user_type = user_type

		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, first_name, last_name, phone, password=None):
		user_type = "ADMIN"
		user = self.create_user(
			email = email,
			first_name = first_name,
			last_name = last_name,
			phone = phone,
			password = password,
			user_type = user_type
			)
		user.is_admin = True
		user.is_superuser = True
		user.is_staff = True

		user.save(using=self._db)
		return user


class StoreWayUser(AbstractBaseUser):
	email = models.EmailField(verbose_name="email address", max_length=60, unique=True)
	first_name = models.CharField(verbose_name="first name", max_length=25)
	last_name = models.CharField(verbose_name="last name", max_length=25)
	phone = models.CharField(max_length=10, verbose_name="phone number")
	date_joined = models.DateTimeField(verbose_name="date joined",auto_now_add=True)
	last_login = models.DateTimeField(verbose_name="last login", auto_now=True)


	user_type = models.CharField(max_length=10, blank = True)

	is_admin = models.BooleanField(default = False)
	is_staff = models.BooleanField(default = False)
	is_active = models.BooleanField(default = True)
	is_superuser = models.BooleanField(default = False)

	USERNAME_FIELD = "email"

	REQUIRED_FIELDS = ['first_name','last_name','phone']

	objects = StoreWayUserManager()

	def __str__(self):
		return self.first_name

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True




