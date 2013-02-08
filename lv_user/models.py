from django.db import models
from django.contrib.auth.models import User

class LVUser(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	date_of_birth = models.DateField(blank=True, null=True)
	skype = models.CharField(blank=True, null=True, max_length = 30, verbose_name='скайп')
	city = models.CharField(blank=True, null=True, max_length = 30, verbose_name='город')
	country = models.CharField(blank=True, null=True, max_length = 30, verbose_name='страна')