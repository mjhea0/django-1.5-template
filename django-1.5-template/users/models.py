from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(max_length=40, unique=True, db_index=True,)
	email = models.EmailField(max_length=100,unique=True,)
	date_joined = models.DateField(auto_now=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def get_full_name(self):
		return self.username

	def get_short_name(self):
		return self.username

	def __unicode__(self):
		return self.username